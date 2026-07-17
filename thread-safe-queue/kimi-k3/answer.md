线程安全的泛型有界阻塞队列


设计思路




底层用 collections.deque 存储（FIFO，append/popleft 均为 O(1)）。


一把互斥锁 + 两个条件变量（not_empty / not_full），两者共享同一把锁，这是经典的生产者–消费者模型（与 CPython queue.Queue 同构）。


等待必须放在 while 循环里重检条件（防止虚假唤醒/被其他线程抢先）。


put 成功后唤醒一个消费者，get 成功后唤醒一个生产者。


超时用 time.monotonic() 计算剩余时间，避免系统时钟回拨影响。




实现 blocking_queue.py


import threading
import time
from collections import deque
from typing import Deque, Generic, Optional, TypeVar

T = TypeVar("T")


class Full(Exception):
    """put 超时或非阻塞 put 时队列已满。"""


class Empty(Exception):
    """get 超时或非阻塞 get 时队列为空。"""


class BoundedBlockingQueue(Generic[T]):
    """线程安全的泛型有界阻塞队列（FIFO）。

    - 队列满时 put 阻塞，直到有消费者取走元素；
    - 队列空时 get 阻塞，直到有生产者放入元素；
    - 支持非阻塞模式与超时模式。
    """

    def __init__(self, maxsize: int) -> None:
        if maxsize <= 0:
            raise ValueError("maxsize 必须是正整数")
        self.maxsize = maxsize
        self._items: Deque[T] = deque()
        self._mutex = threading.Lock()
        # 两个条件变量共享同一把锁
        self._not_empty = threading.Condition(self._mutex)
        self._not_full = threading.Condition(self._mutex)

    # ---------------- 对外接口 ----------------

    def put(self, item: T, block: bool = True,
            timeout: Optional[float] = None) -> None:
        """放入元素；队满时按 block/timeout 策略阻塞或抛 Full。"""
        with self._not_full:
            if not block:
                if self._full():
                    raise Full
            elif timeout is None:
                while self._full():          # while 重检，防虚假唤醒
                    self._not_full.wait()
            else:
                if timeout < 0:
                    raise ValueError("timeout 不能为负数")
                endtime = time.monotonic() + timeout
                while self._full():
                    remaining = endtime - time.monotonic()
                    if remaining <= 0:
                        raise Full
                    self._not_full.wait(remaining)
            self._items.append(item)
            self._not_empty.notify()          # 唤醒一个等待中的消费者

    def get(self, block: bool = True,
            timeout: Optional[float] = None) -> T:
        """取出元素；队空时按 block/timeout 策略阻塞或抛 Empty。"""
        with self._not_empty:
            if not block:
                if self._empty():
                    raise Empty
            elif timeout is None:
                while self._empty():
                    self._not_empty.wait()
            else:
                if timeout < 0:
                    raise ValueError("timeout 不能为负数")
                endtime = time.monotonic() + timeout
                while self._empty():
                    remaining = endtime - time.monotonic()
                    if remaining <= 0:
                        raise Empty
                    self._not_empty.wait(remaining)
            item = self._items.popleft()
            self._not_full.notify()           # 唤醒一个等待中的生产者
            return item

    def put_nowait(self, item: T) -> None:
        self.put(item, block=False)

    def get_nowait(self) -> T:
        return self.get(block=False)

    # ---------------- 状态查询 ----------------

    def qsize(self) -> int:
        with self._mutex:
            return len(self._items)

    def empty(self) -> bool:
        with self._mutex:
            return self._empty()

    def full(self) -> bool:
        with self._mutex:
            return self._full()

    # 内部方法：调用时必须已持有 _mutex
    def _empty(self) -> bool:
        return len(self._items) == 0

    def _full(self) -> bool:
        return len(self._items) >= self.maxsize


单元测试 test_blocking_queue.py



覆盖 6 个场景，其中并发场景 4 个（≥3 满足要求）：



import threading
import time
import unittest

from blocking_queue import BoundedBlockingQueue, Empty, Full


class TestBoundedBlockingQueue(unittest.TestCase):

    # 并发场景 1：单生产者单消费者，容量远小于数据量，
    # 强制 put/get 交替阻塞，验证 FIFO 顺序不丢不重。
    def test_fifo_order_with_concurrent_producer_consumer(self):
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(3)
        n = 2000
        out = []

        def producer():
            for i in range(n):
                q.put(i)

        def consumer():
            for _ in range(n):
                out.append(q.get())

        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start(); t2.start()
        t1.join(timeout=10); t2.join(timeout=10)

        self.assertFalse(t1.is_alive() or t2.is_alive(), "出现死锁")
        self.assertEqual(out, list(range(n)))

    # 并发场景 2：队满时 put 确实阻塞，消费者取走后 put 才被唤醒。
    def test_put_blocks_until_consumer_frees_slot(self):
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(1)
        q.put(1)
        put_done = threading.Event()

        def producer():
            q.put(2)          # 应阻塞，直到主线程取走 1
            put_done.set()

        t = threading.Thread(target=producer)
        t.start()
        time.sleep(0.2)
        self.assertFalse(put_done.is_set())       # 仍在阻塞
        self.assertEqual(q.get(), 1)              # 腾出空位
        t.join(timeout=2)
        self.assertTrue(put_done.is_set())        # 被唤醒并完成
        self.assertEqual(q.get(), 2)

    # 并发场景 3：队空时 get 确实阻塞，生产者放入后 get 才被唤醒。
    def test_get_blocks_until_producer_puts(self):
        q: BoundedBlockingQueue[str] = BoundedBlockingQueue(1)
        got = []

        def consumer():
            got.append(q.get())   # 应阻塞，直到主线程 put

        t = threading.Thread(target=consumer)
        t.start()
        time.sleep(0.2)
        self.assertEqual(got, [])                   # 仍在阻塞
        q.put("hello")
        t.join(timeout=2)
        self.assertEqual(got, ["hello"])

    # 并发场景 4：多生产者多消费者压测，
    # 验证元素不丢失、不重复（无丢失唤醒/无越界写入）。
    def test_multi_producer_multi_consumer(self):
        n_producers, n_consumers, per_producer = 4, 3, 500
        q: BoundedBlockingQueue[object] = BoundedBlockingQueue(10)
        results, lock = [], threading.Lock()
        SENTINEL = object()

        def producer(pid: int):
            for i in range(per_producer):
                q.put(pid * per_producer + i)

        def consumer():
            while True:
                item = q.get()
                if item is SENTINEL:      # 毒丸关闭
                    return
                with lock:
                    results.append(item)

        producers = [threading.Thread(target=producer, args=(p,))
                     for p in range(n_producers)]
        consumers = [threading.Thread(target=consumer)
                     for _ in range(n_consumers)]
        for t in producers + consumers:
            t.start()
        for t in producers:
            t.join(timeout=15)
            self.assertFalse(t.is_alive(), "生产者死锁")
        for _ in range(n_consumers):      # 所有数据入队后投递毒丸
            q.put(SENTINEL)
        for t in consumers:
            t.join(timeout=15)
            self.assertFalse(t.is_alive(), "消费者死锁")

        total = n_producers * per_producer
        self.assertEqual(sorted(results), list(range(total)))

    # 并发场景 5：高并发下队列长度永远不超过 maxsize（不变量）。
    def test_maxsize_invariant_under_contention(self):
        cap = 5
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(cap)
        stop = threading.Event()
        violations = []

        def monitor():
            while not stop.is_set():
                n = q.qsize()
                if not 0 <= n <= cap:
                    violations.append(n)

        def producer():
            for i in range(300):
                q.put(i)

        def consumer():
            for _ in range(300):
                q.get()

        threads = ([threading.Thread(target=producer) for _ in range(3)] +
                   [threading.Thread(target=consumer) for _ in range(3)])
        mon = threading.Thread(target=monitor)
        mon.start()
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=15)
        stop.set()
        mon.join(timeout=2)

        self.assertEqual(violations, [])

    # 非并发语义：超时与非阻塞行为。
    def test_timeout_and_nonblocking(self):
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(1)

        with self.assertRaises(Empty):          # 非阻塞 get 空队列
            q.get_nowait()

        q.put_nowait(1)
        with self.assertRaises(Full):           # 非阻塞 put 满队列
            q.put_nowait(2)

        start = time.monotonic()
        with self.assertRaises(Full):           # put 超时
            q.put(2, timeout=0.3)
        self.assertGreaterEqual(time.monotonic() - start, 0.25)

        self.assertEqual(q.get(), 1)
        start = time.monotonic()
        with self.assertRaises(Empty):          # get 超时
            q.get(timeout=0.3)
        self.assertGreaterEqual(time.monotonic() - start, 0.25)


if __name__ == "__main__":
    unittest.main(verbosity=2)


运行方式


python -m unittest -v test_blocking_queue.py
# 或
pytest test_blocking_queue.py -v


几点说明




为什么用 while 而不是 if 判断后等待：Condition.wait() 可能虚假唤醒，且被唤醒时条件可能已被其他线程改变（例如两个生产者同时被唤醒但只有一个空位），必须循环重检。


为什么 notify() 而非 notify_all()：一次 put 只新增一个元素、一次 get 只腾出一个空位，唤醒一个等待者即可，避免"惊群"；即使唤醒错了对象，等待方也会在 while 中重新入睡，正确性不受影响。


可扩展方向：仿照 queue.Queue 增加 task_done()/join() 支持任务完成追踪，或增加 close() 方法实现优雅关闭（当前测试用"毒丸"哨兵演示了关闭模式）。

