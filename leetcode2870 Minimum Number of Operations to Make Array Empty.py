from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        numOfOperations = 0
        for count in numCount.values():
            if count == 1:
                return -1
            # e.g., for count = 14, 14 // 3 = 4:
            # if remainder is 1, we swap one of the 3 with 2; if remainder is 2, we just use it.
            numOfOperations += count // 3
            if count % 3 != 0:
                numOfOperations += 1

        return numOfOperations
