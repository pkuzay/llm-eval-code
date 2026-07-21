from __future__ import annotations

import threading
from collections import deque
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Full(Exception):
    """队列满时，带超时的 put 在超时后抛出。"""


class Empty(Exception):
    """队列空时，带超时的 get 在超时后抛出。"""


class BoundedBlockingQueue(Generic[T]):
    """
    线程安全的泛型有界阻塞队列。

    - 队满时 put 阻塞，直到有空间或超时。
    - 队空时 get 阻塞，直到有元素或超时。
    - timeout=None 表示无限阻塞。
    - timeout=0 表示非阻塞尝试，失败则抛出 Full/Empty。
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")

        self._capacity = capacity
        self._queue: deque[T] = deque()
        self._cond = threading.Condition()

        # 以下两个计数主要用于单元测试中观察“是否真的阻塞了”。
        # 生产代码不需要可以删除。
        self._waiting_puts = 0
        self._waiting_gets = 0

    def put(self, item: T, timeout: Optional[float] = None) -> None:
        """
        放入元素。

        如果队列已满：
        - timeout=None: 一直阻塞直到有空间。
        - timeout>0: 最多阻塞 timeout 秒，超时抛出 Full。
        - timeout=0: 立即判断，队满抛出 Full。
        """
        if timeout is not None and timeout < 0:
            raise ValueError("timeout must be non-negative")

        with self._cond:
            if len(self._queue) >= self._capacity:
                self._waiting_puts += 1
                try:
                    has_space = self._cond.wait_for(
                        lambda: len(self._queue) < self._capacity,
                        timeout=timeout,
                    )
                finally:
                    self._waiting_puts -= 1

                if not has_space:
                    raise Full("queue is full")

            self._queue.append(item)
            self._cond.notify_all()

    def get(self, timeout: Optional[float] = None) -> T:
        """
        取出元素。

        如果队列为空：
        - timeout=None: 一直阻塞直到有元素。
        - timeout>0: 最多阻塞 timeout 秒，超时抛出 Empty。
        - timeout=0: 立即判断，队空抛出 Empty。
        """
        if timeout is not None and timeout < 0:
            raise ValueError("timeout must be non-negative")

        with self._cond:
            if not self._queue:
                self._waiting_gets += 1
                try:
                    has_item = self._cond.wait_for(
                        lambda: len(self._queue) > 0,
                        timeout=timeout,
                    )
                finally:
                    self._waiting_gets -= 1

                if not has_item:
                    raise Empty("queue is empty")

            item = self._queue.popleft()
            self._cond.notify_all()
            return item

    @property
    def capacity(self) -> int:
        return self._capacity

    def qsize(self) -> int:
        with self._cond:
            return len(self._queue)

    def empty(self) -> bool:
        with self._cond:
            return not self._queue

    def full(self) -> bool:
        with self._cond:
            return len(self._queue) == self._capacity

    @property
    def waiting_puts(self) -> int:
        """当前因队满而阻塞的 put 数量。"""
        with self._cond:
            return self._waiting_puts

    @property
    def waiting_gets(self) -> int:
        """当前因队空而阻塞的 get 数量。"""
        with self._cond:
            return self._waiting_gets
