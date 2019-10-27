
# Remember to check the tricky corner cases, especially the "len(s) < len(p) - p.count('*')"
# The hard part is for when '*' needs to match one more char in s

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False
        if not p:
            return s == ''
        if len(s) < len(p) - p.count('*'):
            return False

        m, n = len(s), len(p)
        dp = [[False for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = True
        for j in xrange(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # dp[i][j - 1] is for when p[j - 1] matches zero char
                    # dp[i - 1][j] is for when p[j - 1] needs to match one more char
                    # even in case that p[j - 1] can match a lot of chars in s, if s[:i] matches
                    # with p[:j], s[:i - 1] should p[:j]. so dp[i][j] can derive from dp[i - 1][j]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[-1][-1]



print Solution().isMatch('adceb', '*a*b')
print Solution().isMatch('acdcb', 'a*c?b')


