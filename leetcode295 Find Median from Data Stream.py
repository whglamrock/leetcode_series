from heapq import *

class MedianFinder:
    def __init__(self):
        self.lo, self.hi = [], []

    def addNum(self, num: int) -> None:
        if not self.lo and not self.hi:
            heappush(self.lo, -num)
            return
        if not self.hi:
            heappush(self.lo, -num)
            heappush(self.hi, -heappop(self.lo))
            return

        if len(self.lo) == len(self.hi):
            heappush(self.hi, num)
            heappush(self.lo, -heappop(self.hi))
        else:
            heappush(self.lo, -num)
            heappush(self.hi, -heappop(self.lo))

    def findMedian(self) -> float:
        if len(self.lo) != len(self.hi):
            return -self.lo[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
