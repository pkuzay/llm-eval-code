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

