from heapq import *


class MedianFinder:
    def __init__(self):
        self.smaller, self.bigger = [], []

    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.bigger):
            heappush(self.bigger, num)
            heappush(self.smaller, -heappop(self.bigger))
        else:
            heappush(self.smaller, -num)
            heappush(self.bigger, -heappop(self.smaller))

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return (-self.smaller[0] + self.bigger[0]) / 2
        else:
            return -self.smaller[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
