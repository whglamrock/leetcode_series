from collections import defaultdict
from typing import List

# A naive "DP" solution actually runs very fast.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumCount = {0: 1}
        for num in nums:
            nextSumCount = defaultdict(int)
            for prevSum in sumCount:
                nextSumCount[prevSum + num] += sumCount[prevSum]
                nextSumCount[prevSum - num] += sumCount[prevSum]
            sumCount = nextSumCount

        return sumCount[target]


'''
# cached dfs solution
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        return self.dfs(0, 0, target)

    @lru_cache(None)
    def dfs(self, i: int, currSum: int, target: int):
        if i == len(self.nums) - 1:
            if currSum == target and self.nums[-1] == 0:
                return 2
            if currSum + self.nums[-1] == target:
                return 1
            if currSum - self.nums[-1] == target:
                return 1
            return 0
        
        return self.dfs(i + 1, currSum + self.nums[i], target) + self.dfs(i + 1, currSum - self.nums[i], target)
'''
