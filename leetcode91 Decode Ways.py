
# the only way to avoid TLE in OJ is to use dp

class Solution(object):
    def numDecodings(self, s):

        if not s: return 0

        dp = [0 for i in xrange(len(s) + 1)]
        dp[0] = 1

        for i in xrange(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # set the lower bound as 10 to avoid checking whether s[i - 2] == '0'
            if i - 2 >= 0 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]