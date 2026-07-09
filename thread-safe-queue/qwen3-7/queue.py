import collections
import threading
import time
import unittest
from typing import Deque, Generic, TypeVar


T = TypeVar("T")


class BoundedBlockingQueue(Generic[T]):
    def __init__(self, maxsize: int):
        if maxsize <= 0:
            raise ValueError("maxsize must be positive")
        self._maxsize = maxsize
        self._queue: Deque[T] = collections.deque()
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: T) -> None:
        with self._not_full:
            while len(self._queue) >= self._maxsize:
                self._not_full.wait()
            self._queue.append(item)
            self._not_empty.notify()

    def get(self) -> T:
        with self._not_empty:
            while not self._queue:
                self._not_empty.wait()
            item = self._queue.popleft()
            self._not_full.notify()
            return item

    def qsize(self) -> int:
        with self._lock:
            return len(self._queue)

    def empty(self) -> bool:
        return self.qsize() == 0


class TestBoundedBlockingQueue(unittest.TestCase):

    # ==========================================
    # 场景 1：生产者阻塞测试（队满时 put 阻塞）
    # ==========================================
    def test_producer_blocks_when_full(self):
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(maxsize=2)
        q.put(1)
        q.put(2)

        producer_unblocked = threading.Event()

        def producer():
            # 尝试放入第 3 个元素，此时队列已满，应该阻塞
            q.put(3)
            producer_unblocked.set()

        t = threading.Thread(target=producer)
        t.start()

        # 给线程一点时间尝试执行 put，确保它已经进入 wait 状态
        time.sleep(0.1)

        # 断言：生产者此时应该处于阻塞状态，Event 未被 set
        self.assertFalse(producer_unblocked.is_set())
        self.assertEqual(q.qsize(), 2)

        # 消费者取出一个元素，释放空间，应该唤醒生产者
        val = q.get()
        self.assertEqual(val, 1)

        # 等待生产者线程结束
        t.join(timeout=1.0)
        self.assertTrue(producer_unblocked.is_set())
        self.assertFalse(t.is_alive())

    # ==========================================
    # 场景 2：消费者阻塞测试（队空时 get 阻塞）
    # ==========================================
    def test_consumer_blocks_when_empty(self):
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(maxsize=5)

        consumer_result = []
        consumer_unblocked = threading.Event()

        def consumer():
            # 队列为空，get 应该阻塞
            val = q.get()
            consumer_result.append(val)
            consumer_unblocked.set()

        t = threading.Thread(target=consumer)
        t.start()

        # 给线程时间进入 wait 状态
        time.sleep(0.1)

        # 断言：消费者此时应该处于阻塞状态
        self.assertFalse(consumer_unblocked.is_set())
        self.assertTrue(q.empty())

        # 生产者放入一个元素，应该唤醒消费者
        q.put(42)

        t.join(timeout=1.0)
        self.assertTrue(consumer_unblocked.is_set())
        self.assertEqual(consumer_result[0], 42)

    # ==========================================
    # 场景 3：高并发吞吐与数据完整性测试 (多生产者/多消费者)
    # ==========================================
    def test_high_concurrency_integrity(self):
        q: BoundedBlockingQueue[object] = BoundedBlockingQueue(maxsize=10)
        num_producers = 5
        num_consumers = 5
        items_per_producer = 1000
        total_items = num_producers * items_per_producer

        produced_items = []
        consumed_items = []
        data_lock = threading.Lock()

        # 哨兵对象：用于通知消费者退出，避免与正常数据（如 None）冲突
        _SENTINEL = object()

        def producer():
            local_produced = []
            thread_id = threading.current_thread().ident or 0
            for i in range(items_per_producer):
                # 生成唯一标识符
                val = thread_id * 100000 + i
                q.put(val)
                local_produced.append(val)
            with data_lock:
                produced_items.extend(local_produced)

        def consumer():
            local_consumed = []
            while True:
                val = q.get()
                if val is _SENTINEL:
                    # 将哨兵重新放入队列，以唤醒其他等待的消费者
                    q.put(_SENTINEL)
                    break
                local_consumed.append(val)
            with data_lock:
                consumed_items.extend(local_consumed)

        producers = [threading.Thread(target=producer) for _ in range(num_producers)]
        consumers = [threading.Thread(target=consumer) for _ in range(num_consumers)]

        # 先启动消费者（它们会立刻阻塞等待数据）
        for t in consumers:
            t.start()
        # 再启动生产者
        for t in producers:
            t.start()

        # 等待所有生产者完成
        for t in producers:
            t.join()

        # 生产结束，放入哨兵通知消费者退出
        q.put(_SENTINEL)

        # 等待所有消费者完成
        for t in consumers:
            t.join()

        # 验证数据完整性：不能丢数据，也不能重复消费数据
        self.assertEqual(len(produced_items), total_items)
        self.assertEqual(len(consumed_items), total_items)
        self.assertEqual(sorted(produced_items), sorted(consumed_items))


if __name__ == "__main__":
    unittest.main()
