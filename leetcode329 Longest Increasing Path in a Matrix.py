from functools import lru_cache
from typing import List

# O(M * N) DFS + memoization solution because each (i, j) will be only visited once.
class Solution:
    def __init__(self):
        self.matrix = None

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs(i, j))
        return ans

    @lru_cache(None)
    def dfs(self, i: int, j: int) -> int:
        up, down, left, right = 0, 0, 0, 0
        num = self.matrix[i][j]

        if i - 1 >= 0 and self.matrix[i - 1][j] > num:
            up = self.dfs(i - 1, j)
        if i + 1 < len(self.matrix) and self.matrix[i + 1][j] > num:
            down = self.dfs(i + 1, j)
        if j - 1 >= 0 and self.matrix[i][j - 1] > num:
            left = self.dfs(i, j - 1)
        if j + 1 < len(self.matrix[0]) and self.matrix[i][j + 1] > num:
            right = self.dfs(i, j + 1)

        ans = 1 + max(up, down, left, right)
        return ans


print(Solution().longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]))
print(Solution().longestIncreasingPath([
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]))
print(Solution().longestIncreasingPath([
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]))
print(Solution().longestIncreasingPath([
    [7, 6, 1, 1],
    [2, 7, 6, 0],
    [1, 3, 5, 1],
    [6, 6, 3, 2]
]))
