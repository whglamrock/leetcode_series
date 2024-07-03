from functools import lru_cache


# Recursion + cache solution. It's the most practical and easiest to remember.
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.dp(m, n, startRow, startColumn, maxMove) % (10 ** 9 + 7)

    @lru_cache(None)
    def dp(self, m: int, n: int, i: int, j: int, maxMove: int) -> int:
        if maxMove < 0:
            return 0
        # already out of grid
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1

        up = self.dp(m, n, i - 1, j, maxMove - 1)
        down = self.dp(m, n, i + 1, j, maxMove - 1)
        left = self.dp(m, n, i, j - 1, maxMove - 1)
        right = self.dp(m, n, i, j + 1, maxMove - 1)

        return up + down + left + right
