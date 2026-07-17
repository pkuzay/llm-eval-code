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
