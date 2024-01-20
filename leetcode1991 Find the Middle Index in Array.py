from collections import deque
from typing import List

# same as lc724: Find Pivot Index
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [nums[0]]
        for i in range(1, n):
            prefixSum.append(prefixSum[-1] + nums[i])
        suffixSum = deque([nums[-1]])
        for i in range(n - 2, -1, -1):
            suffixSum.appendleft(suffixSum[0] + nums[i])

        for i in range(n):
            leftSum, rightSum = 0, 0
            if i > 0:
                leftSum = prefixSum[i - 1]
            if i < n - 1:
                rightSum = suffixSum[i + 1]
            if leftSum == rightSum:
                return i

        return -1
