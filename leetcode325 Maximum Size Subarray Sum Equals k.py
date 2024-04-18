from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSumToIndex = {}
        prefixSum = 0
        maxSubarraySize = 0
        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum == k:
                maxSubarraySize = max(maxSubarraySize, i + 1)
            if prefixSum - k in prefixSumToIndex:
                maxSubarraySize = max(maxSubarraySize, i - prefixSumToIndex[prefixSum - k])

            if prefixSum not in prefixSumToIndex:
                prefixSumToIndex[prefixSum] = i

        return maxSubarraySize
