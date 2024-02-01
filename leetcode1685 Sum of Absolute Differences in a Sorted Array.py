from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        prefixSum = 0
        for i, num in enumerate(nums):
            ans[i] = num * i - prefixSum
            prefixSum += num
        suffixSum = 0
        for i in range(n - 1, -1, -1):
            ans[i] += suffixSum - nums[i] * (n - i - 1)
            suffixSum += nums[i]

        return ans
