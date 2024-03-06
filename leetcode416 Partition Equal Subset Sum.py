from functools import lru_cache
from typing import List

# cached dfs solution, much easier to implement than any "dp".
class Solution:
    def __init__(self):
        self.nums = []

    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2:
            return False
        self.nums = sorted(nums)
        return self.dfs(0, 0, numsSum // 2)

    @lru_cache(None)
    def dfs(self, i: int, currSum: int, target: int) -> bool:
        if currSum == target:
            return True
        if i >= len(self.nums) or currSum > target:
            return False

        if currSum + self.nums[i] > target:
            return False

        return self.dfs(i + 1, currSum + self.nums[i], target) or self.dfs(i + 1, currSum, target)
