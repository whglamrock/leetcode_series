from collections import defaultdict
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSumToIndexes = defaultdict(list)
        prefixSum = 0
        for i, num in enumerate(nums):
            prefixSum = (prefixSum + num) % k
            # entire prefix array is good
            if prefixSum == 0 and i >= 1:
                return True
            if prefixSum in prefixSumToIndexes and i - prefixSumToIndexes[prefixSum][0] >= 2:
                return True
            prefixSumToIndexes[prefixSum].append(i)

        return False
