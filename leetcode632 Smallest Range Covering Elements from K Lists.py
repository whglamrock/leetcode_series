
from heapq import *

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []

        pq = []
        heapify(pq)
        ans = -2147483648, 2147483647

        for i in xrange(len(nums)):
            if nums[i]:
                heappush(pq, [nums[i][0], i, 0])

        # remember how this variable is built, to keep the O(N*logK) time complexity
        right = -2147483648
        for row in nums:
            right = max(right, row[0])

        while pq:
            left, i, j = heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j == len(nums[i]) - 1:
                return ans
            heappush(pq, [nums[i][j + 1], i, j + 1])
            # we don't have to worry about right not being updated because this right will
            # only keep growing (the nums[i] is sorted)
            right = max(right, nums[i][j + 1])



print Solution().smallestRange([[4, 10, 15, 24, 26],[0, 9, 12, 20],[5, 18, 22, 30]])