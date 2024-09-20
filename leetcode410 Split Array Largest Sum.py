from math import ceil
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(ceil(sum(nums) / k), max(nums)), sum(nums)
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return m
            if self.canSplitKArrays(nums, m, k):
                r = m
            else:
                l = m + 1
        return l

    def canSplitKArrays(self, nums: List[int], sumLimit: int, k: int) -> bool:
        splitArraySums = []
        currSum = 0
        for num in nums:
            if currSum + num > sumLimit:
                splitArraySums.append(currSum)
                currSum = num
            else:
                currSum += num

        splitArraySums.append(currSum)
        return len(splitArraySums) <= k
