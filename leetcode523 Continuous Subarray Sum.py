from collections import defaultdict
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSumToIndex = {}
        prefixSum = 0
        for i, num in enumerate(nums):
            prefixSum = (prefixSum + num) % k
            # entire prefix array is good
            if prefixSum == 0 and i >= 1:
                return True
            if prefixSum in prefixSumToIndex and i - prefixSumToIndex[prefixSum] >= 2:
                return True
            if prefixSum not in prefixSumToIndex:
                prefixSumToIndex[prefixSum] = i

        return False
