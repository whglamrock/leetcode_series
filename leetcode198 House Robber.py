
# Idea:
    # f(0) = nums[0]
    # f(1) = max(num[0], num[1])
    # f(k) = max(f(k-2) + nums[k], f(k-1))
# P.S.: O(n) space solution should also work, from which we can optimize to O(1) space tf interviewer asks for it

class Solution:
    def rob(self, nums):

        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now



print Solution().rob([2, 7, 1, 3, 9])
print Solution().rob([1, 2, 3, 1])



'''
# O(N) space solution

class Solution(object):
    def rob(self, nums):

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        # dp[i] means the max amount of money when robbing nums[i]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in xrange(2, n):
            if i < 3:
                dp[i] = dp[i - 2] + nums[i]
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
        
        return max(dp)
'''

