在 Python 中实现一个线程安全的泛型有界阻塞队列，核心在于使用 `threading.Condition`（条件变量）来控制线程的阻塞与唤醒，同时利用 `typing` 模块来提供泛型支持（静态类型检查）。

以下是完整的实现代码以及针对 3 个典型并发场景的单元测试。

### 一、 核心实现代码

```python
import threading
import collections
from typing import TypeVar, Generic

# 定义泛型类型变量
T = TypeVar('T')

class BoundedBlockingQueue(Generic[T]):
    """
    线程安全的泛型有界阻塞队列。
    当队列满时，put 操作会阻塞；当队列空时，get 操作会阻塞。
    """
    def __init__(self, maxsize: int):
        if maxsize <= 0:
            raise ValueError("maxsize must be greater than 0")

        self._maxsize = maxsize
        self._queue = collections.deque()

        # 使用同一个互斥锁来保证条件变量的线程安全
        self._mutex = threading.Lock()
        # 两个条件变量共享同一个底层锁
        self._not_empty = threading.Condition(self._mutex)
        self._not_full = threading.Condition(self._mutex)

    def put(self, item: T) -> None:
        """向队列中添加元素。如果队列已满，则阻塞直到有空间。"""
        with self._not_full:
            # 使用 while 循环而不是 if，以防止虚假唤醒 (spurious wakeup)
            while len(self._queue) >= self._maxsize:
                self._not_full.wait()

            self._queue.append(item)
            # 唤醒一个正在等待获取元素的消费者线程
            self._not_empty.notify()

    def get(self) -> T:
        """从队列中获取元素。如果队列为空，则阻塞直到有元素可用。"""
        with self._not_empty:
            while len(self._queue) == 0:
                self._not_empty.wait()

            item = self._queue.popleft()
            # 唤醒一个正在等待放入元素的生产者线程
            self._not_full.notify()
            return item

    def qsize(self) -> int:
        """返回队列当前的元素数量（非严格实时，仅供参考）。"""
        with self._mutex:
            return len(self._queue)

    def empty(self) -> bool:
        with self._mutex:
            return len(self._queue) == 0
```

---

### 二、 单元测试代码 (3个并发场景)

以下测试使用了 Python 内置的 `unittest` 框架，覆盖了**多对多并发数据完整性**、**队满阻塞与唤醒**、**队空阻塞与唤醒**三个核心场景。

```python
import unittest
import time
import threading

class TestBoundedBlockingQueue(unittest.TestCase):

    # 场景 1：多生产者与多消费者并发（验证线程安全与数据完整性）
    def test_concurrent_producers_and_consumers(self):
        """
        场景描述：启动多个生产者线程和多个消费者线程，
        验证在并发竞争下，数据不会丢失、不会重复，且最终结果正确。
        """
        q = BoundedBlockingQueue[int](maxsize=10)
        produced_data = []
        consumed_data = []
        data_lock = threading.Lock()

        total_items = 1000

        def producer(start_id, count):
            for i in range(count):
                val = start_id * 10000 + i
                q.put(val)
                with data_lock:
                    produced_data.append(val)

        def consumer(count):
            for _ in range(count):
                val = q.get()
                with data_lock:
                    consumed_data.append(val)

        # 启动 4 个生产者，每个生产 250 个数据
        producers = [threading.Thread(target=producer, args=(i, 250)) for i in range(4)]
        # 启动 4 个消费者，每个消费 250 个数据
        consumers = [threading.Thread(target=consumer, args=(250,)) for _ in range(4)]

        for p in producers: p.start()
        for c in consumers: c.start()

        for p in producers: p.join()
        for c in consumers: c.join()

        # 断言：生产的数据和消费的数据完全一致
        self.assertEqual(len(produced_data), total_items)
        self.assertEqual(len(consumed_data), total_items)
        self.assertEqual(sorted(produced_data), sorted(consumed_data))
        self.assertTrue(q.empty())

    # 场景 2：队满阻塞与唤醒（验证 put 阻塞逻辑）
    def test_put_blocks_when_full(self):
        """
        场景描述：将队列填满，验证后续的 put 操作会阻塞。
        当消费者取走一个元素后，验证被阻塞的 put 操作能够被正确唤醒并继续执行。
        """
        q = BoundedBlockingQueue[str](maxsize=2)
        q.put("item_1")
        q.put("item_2")

        put_completed = threading.Event()

        def blocked_put():
            q.put("item_3")  # 此时队列已满，此处应阻塞
            put_completed.set()

        t = threading.Thread(target=blocked_put)
        t.start()

        # 等待一小段时间，确保线程已启动并进入 wait 状态
        time.sleep(0.1)
        self.assertFalse(put_completed.is_set(), "Put 应该在队列满时阻塞")

        # 消费一个元素，腾出空间，应该唤醒阻塞的 put
        item = q.get()
        self.assertEqual(item, "item_1")

        # 验证 put 线程被唤醒并完成
        put_completed.wait(timeout=1.0)
        self.assertTrue(put_completed.is_set(), "Put 应该在 get 腾出空间后被唤醒")
        t.join()
        self.assertEqual(q.qsize(), 2) # 队列中现在应该是 item_2 和 item_3

    # 场景 3：队空阻塞与唤醒（验证 get 阻塞逻辑）
    def test_get_blocks_when_empty(self):
        """
        场景描述：在空队列上执行 get 操作，验证其会阻塞。
        当生产者放入一个元素后，验证被阻塞的 get 操作能够被正确唤醒并获取到数据。
        """
        q = BoundedBlockingQueue[float](maxsize=5)

        get_completed = threading.Event()
        result = []

        def blocked_get():
            item = q.get()  # 此时队列为空，此处应阻塞
            result.append(item)
            get_completed.set()

        t = threading.Thread(target=blocked_get)
        t.start()

        time.sleep(0.1)
        self.assertFalse(get_completed.is_set(), "Get 应该在队列空时阻塞")

        # 放入一个元素，应该唤醒阻塞的 get
        q.put(3.14159)

        # 验证 get 线程被唤醒并完成
        get_completed.wait(timeout=1.0)
        self.assertTrue(get_completed.is_set(), "Get 应该在 put 放入数据后被唤醒")
        self.assertEqual(result[0], 3.14159)
        t.join()
        self.assertTrue(q.empty())

if __name__ == '__main__':
    unittest.main()
```

---

### 三、 设计原理解析

1. **泛型支持 (`Generic[T]`)**：
   Python 是动态类型语言，运行时不会像 Java 那样进行泛型擦除或强制类型检查。但通过继承 `Generic[T]` 并使用 `TypeVar`，我们可以让 IDE（如 PyCharm/VSCode）和静态类型检查工具（如 `mypy`）正确推断 `put` 和 `get` 的参数与返回值类型，提升代码的可维护性。
2. **条件变量 (`threading.Condition`)**：
   代码中使用了两个条件变量 `_not_empty` 和 `_not_full`，它们**共享同一个底层互斥锁 `self._mutex`**。
   * 当 `put` 发现队列满时，调用 `self._not_full.wait()`，这会**原子性地释放锁**并将当前线程挂起。
   * 当 `get` 取走元素后，调用 `self._not_full.notify()`，唤醒等待放入的线程。
3. **为什么使用 `while` 而不是 `if` 进行条件判断？**
   在多线程环境中，操作系统可能会发生**虚假唤醒 (Spurious Wakeup)**（即线程在没有被 `notify` 的情况下意外醒来）。使用 `while len(self._queue) >= self._maxsize:` 可以确保线程醒来后再次检查条件是否真正满足，如果不满足则继续 `wait()`，这是实现并发同步的最佳实践。
4. **`with` 语句管理锁**：
   `with self._not_full:` 等价于获取底层锁，并在代码块执行完毕（或发生异常）时自动释放锁。这避免了手动 `acquire()` 和 `release()` 可能导致的死锁问题。