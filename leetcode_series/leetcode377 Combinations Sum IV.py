# see my own explanation here: https://discuss.leetcode.com/topic/52198/python-solution-dp
# basic idea, number of combination dp[i] is based on dp[0] to dp[i-1]
class Solution(object):
    def combinationSum4(self, nums, target):

        if not nums:
            return 0
        start = min(nums)
        if start > target:
            return 0
        # record number of combinations for i
        dp = [1] + [0] * target
        for i in xrange(target):    # or 'for i in xrange(len(dp)-1)'
            # skip numbers that have no combinations
            if dp[i] != 0:
                for n in nums:
                    if i + n < len(dp):    # or 'if i + n < target + 1'
                        dp[i + n] += dp[i]

        return dp[-1]

Sol = Solution()
print Sol.combinationSum4([1,2,3],6)

# for the follow-up question, when negative numbers in nums, the solution is from:
# https://discuss.leetcode.com/topic/52227/7-liner-in-python-and-follow-up-question/2
# we need to limit the length of combination (e.g., cause 1+(-1)==0, we add infinite [1,-1] pairs...)
'''
# try 'memo=collections.defaultdict(int)', 'memo[1,2] = 1,2', 'print memo'.
# remember this operator
import collections
class Solution(object):
    def combinationSum4WithLength(self, nums, target, length, memo=collections.defaultdict(int)):
        if length <= 0: return 0
        if length == 1: return 1 * (target in nums)  # target in/not in nums, return 1/0
        if (target, length) not in memo:
            for num in nums:
                memo[target, length] += self.combinationSum4(nums, target - num, length - 1)
        return memo[target, length]
'''
