
from heapq import *

class MedianFinder:
    def __init__(self):

        self.small, self.big = [], []

    def addNum(self, num):

        heappush(self.big, num)
        heappush(self.small, -heappop(self.big))
        if len(self.small) > len(self.big):
            heappush(self.big, -heappop(self.small))

    def findMedian(self):

        if len(self.big) == len(self.small):
            # remember how to write the float division. use '2.0', instead of float(a)/float(b)
            return ((-self.small[0]) + self.big[0]) / 2.0
        else:
            return float(self.big[0])



# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()