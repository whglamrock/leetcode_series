from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.windowSum = 0

    def next(self, val: int) -> float:
        while len(self.q) >= self.size:
            self.windowSum -= self.q.popleft()
        self.q.append(val)
        self.windowSum += val
        return self.windowSum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
