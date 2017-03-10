# DP idea from: https://discuss.leetcode.com/topic/51358/java-dp-solution/2
# understand the DP optimal substructure and thinking. This one is a classic DP problem.
class Solution(object):
    def getMoneyAmount(self, n):

        MAX_INT = 2147483647
        if n == 1: return 0

        dp = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]
        for jminusi in xrange(1, n):    # the jminusi defines how big the range is.
            for i in xrange(0, n + 1 - jminusi):
                j = i + jminusi
                dp[i][j] = MAX_INT  # each i for loop only do one j loop.
                for k in xrange(i, j + 1):  # dp[i][j] is defined by all k for loops.
                    if k > i:
                        maxnext1 = dp[i][k - 1]
                    else:
                        maxnext1 = 0
                    if k < j:
                        maxnext2 = dp[k + 1][j]
                    else:
                        maxnext2 = 0
                    dp[i][j] = min(dp[i][j], k + max(maxnext1, maxnext2))

        return dp[1][n]