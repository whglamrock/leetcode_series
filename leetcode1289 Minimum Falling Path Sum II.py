from typing import List


# note that the chosen element in next (i + 1) row isn't necessarily dp[i + 1][j - 1] or dp[i + 1][j + 1].
# It can be any one other than dp[i + 1][j].
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[2147483647 for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, m):
            prefixMin = dp[i - 1][0]
            for j in range(1, n):
                dp[i][j] = prefixMin + grid[i][j]
                prefixMin = min(prefixMin, dp[i - 1][j])
            suffixMin = dp[i - 1][-1]
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(dp[i][j], suffixMin + grid[i][j])
                suffixMin = min(suffixMin, dp[i - 1][j])

        return min(dp[-1])
