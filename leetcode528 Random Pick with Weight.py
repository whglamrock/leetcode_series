from random import randint
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.curr = 0
        self.prefixSum = []
        for i, num in enumerate(w):
            self.curr += num
            self.prefixSum.append(self.curr)

    def pickIndex(self) -> int:
        randomInt = randint(1, self.curr)
        return self.findIndexBiggerOrEqualThan(self.prefixSum, randomInt)

    def findIndexBiggerOrEqualThan(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return l
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
