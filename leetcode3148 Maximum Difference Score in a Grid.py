from typing import List


# Intuition: https://leetcode.com/problems/maximum-difference-score-in-a-grid/solutions/5145704/java-c-python-dp-minimum-on-top-left/
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j] stores the min of the top left area
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]

        ans = -2147483648
        for i in range(m):
            for j in range(n):
                # notice the constraint here: m, n >= 2
                if i == j == 0:
                    continue
                minOfTopLeft = min(dp[i - 1][j] if i - 1 >= 0 else 2147483647, dp[i][j - 1] if j - 1 >= 0 else 2147483647)
                ans = max(ans, grid[i][j] - minOfTopLeft)
                dp[i][j] = min(grid[i][j], minOfTopLeft)

        return ans
