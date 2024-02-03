from functools import lru_cache
from typing import List

# dfs + memoization can achieve O(M * N) time complexity
class Solution:
    def __init__(self):
        self.mat = []

    def longestLine(self, mat: List[List[int]]) -> int:
        self.mat = mat
        longestConsecutiveOnes = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    longestConsecutiveOnes = max(longestConsecutiveOnes, self.longestConsecutiveHorizontal(i, j))
                    longestConsecutiveOnes = max(longestConsecutiveOnes, self.longestConsecutiveVertical(i, j))
                    longestConsecutiveOnes = max(longestConsecutiveOnes, self.longestConsecutiveDiagonal(i, j))
                    longestConsecutiveOnes = max(longestConsecutiveOnes, self.longestConsecutiveAntiDiagonal(i, j))

        return longestConsecutiveOnes

    @lru_cache(None)
    def longestConsecutiveHorizontal(self, i: int, j: int) -> int:
        if self.mat[i][j] == 0:
            return 0
        if j + 1 < len(self.mat[0]) and self.mat[i][j + 1] == 1:
            return 1 + self.longestConsecutiveHorizontal(i, j + 1)
        else:
            return 1

    @lru_cache(None)
    def longestConsecutiveVertical(self, i: int, j: int) -> int:
        if self.mat[i][j] == 0:
            return 0
        if i + 1 < len(self.mat) and self.mat[i + 1][j] == 1:
            return 1 + self.longestConsecutiveVertical(i + 1, j)
        else:
            return 1

    @lru_cache(None)
    def longestConsecutiveDiagonal(self, i: int, j: int) -> int:
        if self.mat[i][j] == 0:
            return 0
        if i + 1 < len(self.mat) and j + 1 < len(self.mat[0]) and self.mat[i + 1][j + 1] == 1:
            return 1 + self.longestConsecutiveDiagonal(i + 1, j + 1)
        else:
            return 1

    @lru_cache(None)
    def longestConsecutiveAntiDiagonal(self, i: int, j: int) -> int:
        if self.mat[i][j] == 0:
            return 0
        if i + 1 < len(self.mat) and j - 1 >= 0 and self.mat[i + 1][j - 1] == 1:
            return 1 + self.longestConsecutiveAntiDiagonal(i + 1, j - 1)
        else:
            return 1
