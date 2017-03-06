# a very special dp practice.
# pay attention to how the recursion is formed.
class Solution(object):
    def longestIncreasingPath(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in xrange(n)] for i in xrange(m)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if (i > 0 and matrix[i - 1][j] > val) else 0,
                    dfs(i + 1, j) if (i < m - 1 and matrix[i + 1][j] > val) else 0,
                    dfs(i, j - 1) if (j > 0 and matrix[i][j - 1] > val) else 0,
                    dfs(i, j + 1) if (j < n - 1 and matrix[i][j + 1] > val) else 0)
            return dp[i][j]

        return max(dfs(x, y) for x in xrange(m) for y in xrange(n))