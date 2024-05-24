from collections import deque
from threading import Semaphore

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.enqSem, self.deqSem = Semaphore(capacity), Semaphore(0)
        self.q = deque()

    def enqueue(self, element: int) -> None:
        self.enqSem.acquire()
        self.q.append(element)
        self.deqSem.release()

    def dequeue(self) -> int:
        self.deqSem.acquire()
        rearElement = self.q.popleft()
        self.enqSem.release()
        return rearElement

    def size(self) -> int:
        return len(self.q)
