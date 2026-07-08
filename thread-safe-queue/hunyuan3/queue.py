import threading
import collections
import time
import unittest
from typing import Generic, TypeVar

T = TypeVar("T")


class BoundedBlockingQueue(Generic[T]):
    """
    线程安全的泛型有界阻塞队列。
    - 队满时 put 阻塞，直到有空闲空间；
    - 队空时 get 阻塞，直到有数据可取。
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self._capacity = capacity
        self._queue: "collections.deque[T]" = collections.deque()

        # 使用同一把锁保护两个条件变量，避免死锁并精准通知
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: T) -> None:
        """将元素放入队列，若队列已满则阻塞。"""
        with self._not_full:
            # 使用 while 防止虚假唤醒（spurious wakeup）
            while len(self._queue) >= self._capacity:
                self._not_full.wait()
            self._queue.append(item)
            # 放入成功后，通知可能在等待"非空"的消费者
            self._not_empty.notify()

    def get(self) -> T:
        """从队列取出一个元素（FIFO），若队列为空则阻塞。"""
        with self._not_empty:
            while len(self._queue) == 0:
                self._not_empty.wait()
            item = self._queue.popleft()
            # 取走成功后，通知可能在等待"不满"的生产者
            self._not_full.notify()
            return item

    def __len__(self) -> int:
        """返回当前队列长度（线程安全）。"""
        with self._not_empty:
            return len(self._queue)


class TestBoundedBlockingQueue(unittest.TestCase):

    def test_single_producer_single_consumer(self):
        """场景1：单生产者 + 单消费者，验证数据完整性与 FIFO 顺序"""
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(10)
        produced = list(range(100))

        def producer():
            for x in produced:
                q.put(x)

        consumed = []
        def consumer():
            for _ in range(100):
                consumed.append(q.get())

        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start(); t2.start()
        t1.join(); t2.join()

        self.assertEqual(consumed, produced)

    def test_get_blocks_when_empty(self):
        """场景2：队列为空时，get 必须阻塞，直到有数据放入"""
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(3)
        got_item = []
        started = threading.Event()

        def consumer():
            started.set()
            got_item.append(q.get())  # 会阻塞

        t = threading.Thread(target=consumer)
        t.start()
        self.assertTrue(started.wait(timeout=1))
        time.sleep(0.1)  # 确保消费者已进入等待

        # 此时消费者线程应当还活着（处于阻塞状态）
        self.assertTrue(t.is_alive())
        self.assertEqual(len(got_item), 0)

        # 生产者放入数据，消费者应被唤醒
        q.put(99)
        t.join(timeout=1)
        self.assertFalse(t.is_alive())
        self.assertEqual(got_item[0], 99)

    def test_put_blocks_when_full(self):
        """场景3：队列已满时，put 必须阻塞，直到消费者腾出空间"""
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(2)
        q.put(1)
        q.put(2)  # 此时队列已满

        started = threading.Event()
        finished = threading.Event()

        def producer():
            started.set()
            q.put(3)  # 会阻塞
            finished.set()

        t = threading.Thread(target=producer)
        t.start()
        self.assertTrue(started.wait(timeout=1))
        time.sleep(0.1)

        # 生产者应该还在阻塞中
        self.assertTrue(t.is_alive())
        self.assertFalse(finished.is_set())

        # 消费者取走一个，腾出空间
        self.assertEqual(q.get(), 1)

        # 生产者被唤醒并完成
        self.assertTrue(finished.wait(timeout=1))
        t.join(timeout=1)
        self.assertFalse(t.is_alive())

        # 验证所有数据最终都在队列中
        self.assertEqual(q.get(), 2)
        self.assertEqual(q.get(), 3)

    def test_multiple_producers_consumers(self):
        """场景4：多生产者 + 多消费者，验证并发安全、无丢失/重复、容量不越界"""
        capacity = 5
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity)
        num_producers = 4
        num_consumers = 3
        items_per_producer = 25
        total_items = num_producers * items_per_producer
        poison = -1  # 用负数作为"毒药"通知消费者退出

        max_len = 0
        len_lock = threading.Lock()

        def producer(pid):
            for i in range(items_per_producer):
                q.put(pid * 1000 + i)
                with len_lock:
                    if len(q) > max_len:
                        max_len = len(q)

        results = []
        res_lock = threading.Lock()

        def consumer():
            while True:
                item = q.get()
                if item == poison:
                    break
                with res_lock:
                    results.append(item)

        producers = [threading.Thread(target=producer, args=(i,)) for i in range(num_producers)]
        consumers = [threading.Thread(target=consumer) for _ in range(num_consumers)]

        for c in consumers: c.start()
        for p in producers: p.start()
        for p in producers: p.join()

        # 所有生产者完成后，投放毒药让消费者安全退出
        for _ in range(num_consumers):
            q.put(poison)
        for c in consumers: c.join()

        # 验证所有数据被正确且唯一地消费
        self.assertEqual(len(results), total_items)
        self.assertEqual(len(set(results)), total_items)
        # 验证队列在任何时刻都没有超过声明容量
        self.assertLessEqual(max_len, capacity)


if __name__ == "__main__":
    unittest.main()
