from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = []
        for weight in w:
            if not self.prefixSum:
                self.prefixSum.append(weight)
            else:
                self.prefixSum.append(weight + self.prefixSum[-1])

    def pickIndex(self) -> int:
        target = randint(1, self.prefixSum[-1])
        return self.findMinIndexBiggerOrEqualThan(self.prefixSum, target)

    def findMinIndexBiggerOrEqualThan(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
