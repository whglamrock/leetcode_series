from functools import lru_cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return self.dfs(row, column, k, n)

    @lru_cache(None)
    def dfs(self, i: int, j: int, k: int, n: int) -> float:
        if k == 0:
            return 1
        if i < 0 or j < 0 or i >= n or j >= n:
            return 0

        probability = 0
        if i - 1 >= 0 and j - 2 >= 0:
            probability += 0.125 * self.dfs(i - 1, j - 2, k - 1, n)
        if i - 2 >= 0 and j - 1 >= 0:
            probability += 0.125 * self.dfs(i - 2, j - 1, k - 1, n)
        if i - 2 >= 0 and j + 1 < n:
            probability += 0.125 * self.dfs(i - 2, j + 1, k - 1, n)
        if i - 1 >= 0 and j + 2 < n:
            probability += 0.125 * self.dfs(i - 1, j + 2, k - 1, n)
        if i + 1 < n and j - 2 >= 0:
            probability += 0.125 * self.dfs(i + 1, j - 2, k - 1, n)
        if i + 2 < n and j - 1 >= 0:
            probability += 0.125 * self.dfs(i + 2, j - 1, k - 1, n)
        if i + 2 < n and j + 1 < n:
            probability += 0.125 * self.dfs(i + 2, j + 1, k - 1, n)
        if i + 1 < n and j + 2 < n:
            probability += 0.125 * self.dfs(i + 1, j + 2, k - 1, n)

        return probability
