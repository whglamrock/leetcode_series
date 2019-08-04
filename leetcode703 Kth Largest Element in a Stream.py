
from heapq import *

# note the trap that len(nums) can == k - 1

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pq = nums
        self.k = k
        # it's important to heapify first! otherwise heappop(self.pq) doesn't guarantee always popping the smallest number
        heapify(self.pq)
        # make sure it's a size of k priority queue
        while len(self.pq) > k:
            heappop(self.pq)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.pq, val)
        # note that nums is only guaranteed to have at least k numbers after the add operation
        while len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)