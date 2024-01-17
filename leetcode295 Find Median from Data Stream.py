from heapq import *

class MedianFinder:

    def __init__(self):
        self.left = []
        heapify(self.left)
        self.right = []
        heapify(self.right)

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heappush(self.left, -num)
            return
        # left will always have 0 or 1 more number than right
        if not self.right:
            prevNum = heappop(self.left)
            prevNum = -prevNum
            heappush(self.left, -min(prevNum, num))
            heappush(self.right, max(prevNum, num))
            return

        maxOfLeft = -self.left[0]
        if len(self.left) == len(self.right):
            minOfRight = self.right[0]
            if num <= maxOfLeft or num <= minOfRight:
                heappush(self.left, -num)
            else:
                heappop(self.right)
                heappush(self.left, -minOfRight)
                heappush(self.right, num)
        else:
            if num >= maxOfLeft:
                heappush(self.right, num)
            else:
                heappop(self.left)
                heappush(self.left, -num)
                heappush(self.right, maxOfLeft)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        else:
            return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
