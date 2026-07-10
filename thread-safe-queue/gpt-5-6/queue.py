from __future__ import annotations

import threading
import unittest
from collections import Counter, deque
from typing import Deque, Generic, TypeVar


T = TypeVar("T")


class BoundedBlockingQueue(Generic[T]):
    """线程安全的泛型有界阻塞队列。"""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        self._capacity = capacity
        self._queue: Deque[T] = deque()

        # not_empty 和 not_full 共享同一把互斥锁，
        # 保证检查条件和修改队列状态是原子操作。
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: T) -> None:
        """
        将元素放入队列。

        当队列已满时阻塞，直到有消费者取走元素。
        """
        with self._not_full:
            while len(self._queue) >= self._capacity:
                self._not_full.wait()

            self._queue.append(item)

            # 队列由空变为非空，或者增加了可消费元素。
            self._not_empty.notify()

    def get(self) -> T:
        """
        从队列头部取出并返回元素。

        当队列为空时阻塞，直到生产者放入元素。
        """
        with self._not_empty:
            while not self._queue:
                self._not_empty.wait()

            item = self._queue.popleft()

            # 队列由满变为非满，或者增加了可用空间。
            self._not_full.notify()
            return item

    def qsize(self) -> int:
        """返回当前队列长度。"""
        with self._lock:
            return len(self._queue)

    def empty(self) -> bool:
        """判断队列是否为空。"""
        with self._lock:
            return not self._queue

    def full(self) -> bool:
        """判断队列是否已满。"""
        with self._lock:
            return len(self._queue) >= self._capacity

    @property
    def capacity(self) -> int:
        return self._capacity


class TestBoundedBlockingQueue(unittest.TestCase):

    def test_put_blocks_when_queue_is_full(self) -> None:
        """场景一：队满时，生产者应阻塞，直到消费者取走元素。"""
        queue = BoundedBlockingQueue[int](capacity=1)
        queue.put(1)

        producer_started = threading.Event()
        producer_finished = threading.Event()

        def producer() -> None:
            producer_started.set()
            queue.put(2)
            producer_finished.set()

        thread = threading.Thread(target=producer)
        thread.start()

        self.assertTrue(producer_started.wait(timeout=1))

        # 队列仍然是满的，因此 put(2) 不应完成。
        self.assertFalse(producer_finished.wait(timeout=0.1))

        self.assertEqual(queue.get(), 1)

        # get() 释放空间后，生产者应继续执行。
        self.assertTrue(producer_finished.wait(timeout=1))
        self.assertEqual(queue.get(), 2)

        thread.join(timeout=1)
        self.assertFalse(thread.is_alive())

    def test_get_blocks_when_queue_is_empty(self) -> None:
        """场景二：队空时，消费者应阻塞，直到生产者放入元素。"""
        queue = BoundedBlockingQueue[str](capacity=2)

        consumer_started = threading.Event()
        consumer_finished = threading.Event()
        result: list[str] = []

        def consumer() -> None:
            consumer_started.set()
            result.append(queue.get())
            consumer_finished.set()

        thread = threading.Thread(target=consumer)
        thread.start()

        self.assertTrue(consumer_started.wait(timeout=1))

        # 队列为空，因此 get() 不应完成。
        self.assertFalse(consumer_finished.wait(timeout=0.1))

        queue.put("hello")

        self.assertTrue(consumer_finished.wait(timeout=1))
        self.assertEqual(result, ["hello"])

        thread.join(timeout=1)
        self.assertFalse(thread.is_alive())

    def test_multiple_producers_and_consumers(self) -> None:
        """场景三：多个生产者和消费者并发工作，不丢失、不重复元素。"""
        queue = BoundedBlockingQueue[object](capacity=5)

        producer_count = 4
        consumer_count = 3
        items_per_producer = 100
        sentinel = object()

        consumed: list[tuple[int, int]] = []
        consumed_lock = threading.Lock()

        def producer(producer_id: int) -> None:
            for sequence in range(items_per_producer):
                queue.put((producer_id, sequence))

        def consumer() -> None:
            while True:
                item = queue.get()

                if item is sentinel:
                    return

                with consumed_lock:
                    consumed.append(item)  # type: ignore[arg-type]

        consumers = [
            threading.Thread(target=consumer)
            for _ in range(consumer_count)
        ]
        producers = [
            threading.Thread(target=producer, args=(producer_id,))
            for producer_id in range(producer_count)
        ]

        for thread in consumers:
            thread.start()

        for thread in producers:
            thread.start()

        for thread in producers:
            thread.join(timeout=5)
            self.assertFalse(thread.is_alive(), "生产者线程可能发生死锁")

        # 每个消费者对应一个退出标记。
        for _ in range(consumer_count):
            queue.put(sentinel)

        for thread in consumers:
            thread.join(timeout=5)
            self.assertFalse(thread.is_alive(), "消费者线程可能发生死锁")

        expected = [
            (producer_id, sequence)
            for producer_id in range(producer_count)
            for sequence in range(items_per_producer)
        ]

        self.assertEqual(len(consumed), len(expected))
        self.assertEqual(Counter(consumed), Counter(expected))
        self.assertTrue(queue.empty())

    def test_fifo_order_for_single_producer_and_consumer(self) -> None:
        """场景四：单生产者、单消费者并发时保持 FIFO 顺序。"""
        queue = BoundedBlockingQueue[int](capacity=3)
        item_count = 100
        consumed: list[int] = []

        def producer() -> None:
            for item in range(item_count):
                queue.put(item)

        def consumer() -> None:
            for _ in range(item_count):
                consumed.append(queue.get())

        consumer_thread = threading.Thread(target=consumer)
        producer_thread = threading.Thread(target=producer)

        consumer_thread.start()
        producer_thread.start()

        producer_thread.join(timeout=5)
        consumer_thread.join(timeout=5)

        self.assertFalse(producer_thread.is_alive())
        self.assertFalse(consumer_thread.is_alive())
        self.assertEqual(consumed, list(range(item_count)))


if __name__ == "__main__":
    unittest.main()
