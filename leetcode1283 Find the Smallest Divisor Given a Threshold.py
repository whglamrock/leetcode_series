from math import ceil
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            divisionSum = sum(ceil(num / m) for num in nums)
            if divisionSum <= threshold:
                r = m
            else:
                l = m + 1

        return l
