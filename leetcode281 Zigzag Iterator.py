from collections import deque
from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.values = deque()
        v1, v2 = deque(v1), deque(v2)
        while v1 and v2:
            self.values.append(v1.popleft())
            self.values.append(v2.popleft())

        while v1:
            self.values.append(v1.popleft())
        while v2:
            self.values.append(v2.popleft())

    def next(self) -> int:
        return self.values.popleft()

    def hasNext(self) -> bool:
        return len(self.values) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
