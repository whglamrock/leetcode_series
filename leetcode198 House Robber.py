from typing import List

# Use two pointers (take, skip) to achieve O(1) space is also doable but O(n) space solution is good enough
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp1 stores the max money you can rob if you rob i
        dp1 = [0] * n
        # dp2 stores the max money you can rob if you don't rob i
        dp2 = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                dp1[i] = num
                continue
            # if you rob i, you must not rob i - 1
            dp1[i] = dp2[i - 1] + num
            dp2[i] = max(dp2[i - 1], dp1[i - 1])

        return max(dp1[-1], dp2[-1])


print(Solution().rob([2, 7, 1, 3, 9]))
print(Solution().rob([1, 2, 3, 1]))



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

