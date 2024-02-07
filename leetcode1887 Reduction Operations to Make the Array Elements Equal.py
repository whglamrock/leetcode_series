from collections import Counter
from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        sortedDistinctNums = sorted(set(nums))
        ans = 0
        for i in range(1, len(sortedDistinctNums)):
            ans += i * numCount[sortedDistinctNums[i]]

        return ans
