from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeroCount1, zeroCount2 = 0, 0
        for num in nums1:
            if num == 0:
                zeroCount1 += 1
        for num in nums2:
            if num == 0:
                zeroCount2 += 1

        originalSum1, originalSum2 = sum(nums1), sum(nums2)
        if zeroCount1 == 0 and zeroCount2 == 0:
            if originalSum1 == originalSum2:
                return originalSum2
            else:
                return -1
        elif zeroCount1 == 0:
            if originalSum2 + zeroCount2 > originalSum1:
                return -1
            else:
                return originalSum1
        elif zeroCount2 == 0:
            if originalSum1 + zeroCount1 > originalSum2:
                return -1
            else:
                return originalSum2
        else:
            return max(originalSum1 + zeroCount1, originalSum2 + zeroCount2)
