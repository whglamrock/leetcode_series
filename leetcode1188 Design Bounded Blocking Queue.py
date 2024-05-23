from collections import deque
from threading import Semaphore

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.push = Semaphore(capacity)
        self.pull = Semaphore(0)
        self.q = deque()

    def enqueue(self, element: int) -> None:
        self.push.acquire()
        self.q.append(element)
        self.pull.release()

    def dequeue(self) -> int:
        self.pull.acquire()
        rearElement = self.q.popleft()
        self.push.release()
        return rearElement

    def size(self) -> int:
        return len(self.q)
