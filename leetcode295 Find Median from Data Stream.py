
from heapq import *

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller, self.bigger = [], []
        heapify(self.smaller)
        heapify(self.bigger)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # must do this step to keep both heap updated
        heappush(self.bigger, num)
        heappush(self.smaller, -heappop(self.bigger))

        # always make sure len(bigger) == len(smaller) or len(bigger) = len(smaller) + 1
        while len(self.smaller) > len(self.bigger):
            heappush(self.bigger, -heappop(self.smaller))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smaller) == len(self.bigger):
            # remember how to write the float division; use '2.0' directly instead of float(a) / float(b)
            return (-self.smaller[0] + self.bigger[0]) / 2.0
        else:
            return float(self.bigger[0])



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()