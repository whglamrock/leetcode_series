
# only dp can achieve O(N) time complexity. We can optimize to O(1) space but not necessary here

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in xrange(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= 2:
                dp[i] += dp[i - 2]

        return dp[-1]



print Solution().climbStairs(7)
print Solution().climbStairs(19)