
# Time complexity will have to be at least O(mn), but space complexity can be improved to O(n).
# However, in real interview, getting out the below solution is very enough

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        m, n = len(s), len(t)
        # dp[i][j] means the total number of ways for s[:i] and t[:j] to match
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        # do not also set dp[0][j] here because it's s that needs to remove chars, not t
        for i in xrange(m + 1):
            dp[i][0] = 1

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                # we can simply populate the matching status of (s[:i - 1] & t[:j]) by removing s[i - 1]
                dp[i][j] = dp[i - 1][j]
                # normal case
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]



print Solution().numDistinct("babagbag", "bag")
print Solution().numDistinct("rabbbit", "rabbit")