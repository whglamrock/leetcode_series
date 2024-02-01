from math import ceil
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefixSums = []
        for num in nums:
            if not prefixSums:
                prefixSums.append(num)
            else:
                prefixSums.append(num + prefixSums[-1])

        l, r = max(ceil(sum(nums) / k), max(nums)), sum(nums)
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return m
            if self.canSplitKArrays(prefixSums, m, k):
                r = m
            else:
                l = m + 1
        return l

    def canSplitKArrays(self, prefixSums: List[int], sumLimit: int, k: int) -> bool:
        splitArrays = []
        i = 0
        n = len(prefixSums)
        while i < n:
            prevPrefixSum = 0 if not splitArrays else splitArrays[-1]
            while i + 1 < n and prefixSums[i + 1] - prevPrefixSum <= sumLimit:
                i += 1
            splitArrays.append(prefixSums[i])
            i += 1
        return len(splitArrays) <= k
