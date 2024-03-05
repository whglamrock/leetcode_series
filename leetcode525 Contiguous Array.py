from typing import List

# Remember this trick of changing 0 to -1 then use prefixSum
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = -1

        prefixSum = 0
        prefixSumToIndex = {}
        maxLen = 0
        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum == 0:
                maxLen = max(maxLen, i + 1)
            elif prefixSum in prefixSumToIndex:
                maxLen = max(maxLen, i - prefixSumToIndex[prefixSum])

            if prefixSum not in prefixSumToIndex:
                prefixSumToIndex[prefixSum] = i

        return maxLen


print(Solution().findMaxLength([0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))
