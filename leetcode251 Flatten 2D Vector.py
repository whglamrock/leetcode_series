from collections import deque
from typing import List

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.nums = deque()
        for vector in vec:
            self.nums += vector

    def next(self) -> int:
        return self.nums.popleft()

    def hasNext(self) -> bool:
        return len(self.nums) > 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
