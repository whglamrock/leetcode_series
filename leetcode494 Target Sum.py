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
    def dfs(self, curr: int, i: int, target: int) -> int:
        if i == len(self.nums):
            if curr == target:
                return 1
            return 0
        
        count = 0
        positiveNext = curr + self.nums[i]
        count += self.dfs(positiveNext, i + 1, target)

        negativeNext = curr - self.nums[i]
        count += self.dfs(negativeNext, i + 1, target)

        return count
'''
