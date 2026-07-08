这是一个基于 Python 实现的线程安全、泛型有界阻塞队列。我们使用 `threading.Condition` 来实现等待/通知机制，使用 `collections.deque` 来实现高效的双端队列操作，并使用 `typing.TypeVar` 和 `Generic` 来实现泛型。

### 1. 队列实现代码

```python
import threading
import collections
from typing import TypeVar, Generic, Optional
import queue # 仅复用其 Full/Empty 异常

# 定义泛型类型变量
T = TypeVar('T')

class BoundedBlockingQueue(Generic[T]):
    """
    线程安全的泛型有界阻塞队列
    """
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self._queue: collections.deque[T] = collections.deque()
        # Condition 内部自带一把锁，用于保护共享资源 _queue
        self._cond = threading.Condition()

    def put(self, item: T, timeout: Optional[float] = None) -> None:
        """
        将元素放入队列。如果队列已满，则阻塞直到有空间可用或超时。
        """
        with self._cond:
            # wait_for 会在被唤醒后重新检查条件，防止虚假唤醒
            if not self._cond.wait_for(lambda: len(self._queue) < self.capacity, timeout=timeout):
                raise queue.Full("Queue is full and timeout elapsed")

            self._queue.append(item)
            # 通知可能在等待获取元素的消费者线程
            self._cond.notify()

    def get(self, timeout: Optional[float] = None) -> T:
        """
        从队列中取出并移除头部元素。如果队列为空，则阻塞直到有元素可用或超时。
        """
        with self._cond:
            if not self._cond.wait_for(lambda: len(self._queue) > 0, timeout=timeout):
                raise queue.Empty("Queue is empty and timeout elapsed")

            item = self._queue.popleft()
            # 通知可能在等待空位的生产者线程
            self._cond.notify()
            return item

    def size(self) -> int:
        """获取当前队列大小"""
        with self._cond:
            return len(self._queue)

```

### 2. 并发单元测试

以下是 3 个并发场景的单元测试，分别测试：**多生产者多消费者基础并发**、**队满时生产者阻塞**、**队空时消费者阻塞**。

```python
import unittest
import threading
import time
from typing import List

class TestBoundedBlockingQueue(unittest.TestCase):

    def test_1_concurrent_producer_consumer(self):
        """
        场景1：多生产者、多消费者并发读写
        验证数据不丢失、不重复、线程安全。
        """
        capacity = 10
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity)
        num_producers = 4
        num_consumers = 4
        items_per_producer = 50
        total_items = num_producers * items_per_producer

        produced_items: List[int] = []
        consumed_items: List[int] = []
        # 用于保护 list 操作的锁
        list_lock = threading.Lock()

        def producer(pid: int):
            for i in range(items_per_producer):
                item = pid * 1000 + i
                q.put(item)
                with list_lock:
                    produced_items.append(item)

        def consumer():
            for _ in range(total_items // num_consumers):
                item = q.get(timeout=2) # 设置超时防止死锁卡死测试
                with list_lock:
                    consumed_items.append(item)

        threads = []
        for i in range(num_producers):
            threads.append(threading.Thread(target=producer, args=(i,)))
        for i in range(num_consumers):
            threads.append(threading.Thread(target=consumer))

        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)

        # 断言所有线程都已执行完毕
        for t in threads:
            self.assertFalse(t.is_alive(), "Thread is still alive, possible deadlock")

        # 断言生产消费数量正确
        self.assertEqual(len(produced_items), total_items)
        self.assertEqual(len(consumed_items), total_items)

        # 断言消费的元素与生产的元素完全一致（无丢失无重复）
        self.assertCountEqual(produced_items, consumed_items)
        self.assertEqual(q.size(), 0)

    def test_2_put_blocks_when_full(self):
        """
        场景2：队列已满时，put 操作阻塞，直到有元素被 get 后才恢复。
        """
        capacity = 2
        q: BoundedBlockingQueue[str] = BoundedBlockingQueue(capacity)
        event_was_blocked = threading.Event()

        def producer():
            q.put("A")
            q.put("B") # 此时队列已满
            # 如果下面这行不阻塞，event会被立即设置
            event_was_blocked.set()
            q.put("C") # 这一步应该阻塞，直到主线程取走一个元素

        t = threading.Thread(target=producer)
        t.start()

        # 等待一小段时间，让生产者执行到准备 put("C")
        time.sleep(0.1)

        # 此时队列应该满了，且 event 已经被 set，但线程仍存活（因为阻塞在 put("C")）
        self.assertTrue(event_was_blocked.is_set(), "Producer should have reached put('C')")
        self.assertTrue(t.is_alive(), "Producer thread should be blocked because queue is full")
        self.assertEqual(q.size(), capacity)

        # 取走一个元素，释放空间
        item = q.get()
        self.assertEqual(item, "A")

        # 等待生产者线程结束，说明阻塞被解除了
        t.join(timeout=2)
        self.assertFalse(t.is_alive(), "Producer should have unblocked and finished")
        self.assertEqual(q.size(), capacity) # 队列里应该剩下 B 和 C

    def test_3_get_blocks_when_empty(self):
        """
        场景3：队列为空时，get 操作阻塞，直到有元素被 put 后才恢复。
        """
        capacity = 2
        q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity)
        received_item = None
        event_consumer_started = threading.Event()

        def consumer():
            event_consumer_started.set()
            nonlocal received_item
            # 队列为空，此处应该阻塞
            received_item = q.get()

        t = threading.Thread(target=consumer)
        t.start()

        # 等待消费者启动并尝试 get
        event_consumer_started.wait(timeout=1)
        time.sleep(0.1)

        # 断言线程被阻塞，且未获取到数据
        self.assertTrue(t.is_alive(), "Consumer thread should be blocked because queue is empty")
        self.assertIsNone(received_item)
        self.assertEqual(q.size(), 0)

        # 放入一个元素，唤醒消费者
        q.put(99)

        # 等待消费者线程结束
        t.join(timeout=2)
        self.assertFalse(t.is_alive(), "Consumer should have unblocked and finished")

        # 断言消费者成功获取到了刚才放入的元素
        self.assertEqual(received_item, 99)
        self.assertEqual(q.size(), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

### 设计说明：
1. **并发控制核心 (`Condition`)**：使用 `threading.Condition()` 是最佳实践。它的 `wait_for(predicate)` 方法内部自动处理了循环检查条件和防止虚假唤醒的逻辑，比手写 `while + wait()` 更加优雅安全。
2. **泛型 (`TypeVar` & `Generic`)**：通过继承 `Generic[T]`，该类在 IDE（如 PyCharm, VSCode）中可以获得完整的类型推断提示，例如声明 `BoundedBlockingQueue[int]` 后，put 入 str 会在静态检查时报错。
3. **超时机制**：`put` 和 `get` 都支持 `timeout` 参数。这是并发编程中的好习惯，在单元测试中也起到了防止死锁导致测试进程永久挂起的作用。
4. **双向通知 (`notify`)**：`put` 成功后 `notify` 唤醒等待 `get` 的线程；`get` 成功后 `notify` 唤醒等待 `put` 的线程。这里使用 `notify()` 而非 `notify_all()` 是因为每次操作只腾出/占用了一个位置，只需唤醒一个对应的等待线程即可，减少惊群效应。