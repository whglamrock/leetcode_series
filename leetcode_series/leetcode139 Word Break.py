# O(N^2) classic dp solution.
class Solution(object):
    def wordBreak(self, s, wordDict):

        if not s: return False

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in xrange(1, len(s) + 1):
            for j in xrange(i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                # to prune duplicated branches, avoid TLE.
                if dp[i] == 1: break

        return dp[-1] == 1

