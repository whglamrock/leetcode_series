
# the key is to find the optimal substructure, and update the dp backward

from collections import Counter
class Solution(object):
    def findMaxForm(self, strs, m, n):

        if not strs: return 0
        dp = [[0] * (n + 1) for _ in xrange(m + 1)]

        for string in strs:
            count = Counter(string)
            zero, one = count['0'], count['1']
            # we need to update the dp backward because for a same string,
            #   previous updated dp values should not affect the dp values in this round
            # i.e., all dp values are only influenced by the previous loop
            for i in xrange(m, -1, -1):
                for j in xrange(n, -1, -1):
                    if i >= zero and j >= one:
                        dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)

        return dp[m][n]