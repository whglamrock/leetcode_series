
# see idea from: https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)

class Solution(object):
    def numTrees(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        g = [0 for i in xrange(n + 1)]
        g[0], g[1] = 1, 1

        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                g[i] += g[j - 1] * g[i - j]

        return g[n]