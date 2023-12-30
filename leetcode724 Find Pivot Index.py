from typing import List
from collections import deque

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

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


print(Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex(nums=[1, 2, 3]))
print(Solution().pivotIndex(nums=[2, 1, -1]))
print(Solution().pivotIndex(nums=[4]))
