from __future__ import annotations

import threading
import time
import unittest
from typing import Any

from blocking_queue import BoundedBlockingQueue, Empty, Full


def wait_until(predicate, timeout: float = 5.0, interval: float = 0.001) -> bool:
    """
    等待 predicate() 返回 True。

    用于测试中避免使用过长的固定 sleep，
    例如等待某个线程真的进入阻塞状态。
    """
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if predicate():
            return True
        time.sleep(interval)
    return False


class TestBoundedBlockingQueue(unittest.TestCase):

    def test_multi_producer_multi_consumer(self) -> None:
        num_producers = 4
        items_per_producer = 250
        num_consumers = 3
        total = num_producers * items_per_producer

        q: BoundedBlockingQueue[Any] = BoundedBlockingQueue(capacity=32)

        results: list[Any] = []
        results_lock = threading.Lock()

        sentinel = object()

        def producer(pid: int) -> None:
            base = pid * items_per_producer
            for i in range(items_per_producer):
                q.put(base + i)

        def consumer() -> None:
            while True:
                item = q.get()
                if item is sentinel:
                    break
                with results_lock:
                    results.append(item)

        producer_threads = [
            threading.Thread(target=producer, args=(pid,), daemon=True)
            for pid in range(num_producers)
        ]
        consumer_threads = [
            threading.Thread(target=consumer, daemon=True)
            for _ in range(num_consumers)
        ]

        for t in consumer_threads:
            t.start()

        for t in producer_threads:
            t.start()

        for t in producer_threads:
            t.join(timeout=10)

        for _ in range(num_consumers):
            q.put(sentinel, timeout=10)

        for t in consumer_threads:
            t.join(timeout=10)

        for t in producer_threads + consumer_threads:
            self.assertFalse(t.is_alive())

        expected = set(range(total))

        self.assertEqual(len(results), total)
        self.assertEqual(set(results), expected)

    def test_put_blocks_when_full(self) -> None:
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity=2)

        q.put(1)
        q.put(2)
        self.assertTrue(q.full())

        done = threading.Event()

        def blocked_put() -> None:
            q.put(3)
            done.set()

        t = threading.Thread(target=blocked_put, daemon=True)
        t.start()

        self.assertTrue(
            wait_until(lambda: q.waiting_puts == 1),
            "put did not block when queue was full",
        )

        self.assertTrue(t.is_alive())
        self.assertTrue(q.full())
        self.assertEqual(q.qsize(), 2)

        self.assertEqual(q.get(), 1)

        self.assertTrue(
            done.wait(timeout=5),
            "blocked put did not resume after space was available",
        )

        t.join(timeout=5)
        self.assertFalse(t.is_alive())

        self.assertEqual(q.qsize(), 2)
        self.assertEqual(q.get(), 2)
        self.assertEqual(q.get(), 3)
        self.assertTrue(q.empty())

    def test_get_blocks_when_empty(self) -> None:
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity=2)

        received: list[int] = []
        done = threading.Event()

        def blocked_get() -> None:
            received.append(q.get())
            done.set()

        t = threading.Thread(target=blocked_get, daemon=True)
        t.start()

        self.assertTrue(
            wait_until(lambda: q.waiting_gets == 1),
            "get did not block when queue was empty",
        )

        self.assertTrue(t.is_alive())
        self.assertTrue(q.empty())

        q.put(42)

        self.assertTrue(
            done.wait(timeout=5),
            "blocked get did not resume after item was put",
        )

        t.join(timeout=5)
        self.assertFalse(t.is_alive())

        self.assertEqual(received, [42])
        self.assertTrue(q.empty())

    def test_timeout_raises_full_and_empty(self) -> None:
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity=1)

        q.put(1)
        self.assertTrue(q.full())

        with self.assertRaises(Full):
            q.put(2, timeout=0.05)

        self.assertEqual(q.qsize(), 1)

        empty_q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity=1)
        self.assertTrue(empty_q.empty())

        with self.assertRaises(Empty):
            empty_q.get(timeout=0.05)

        self.assertTrue(empty_q.empty())


if __name__ == "__main__":
    unittest.main()
