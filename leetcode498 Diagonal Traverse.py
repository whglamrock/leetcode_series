from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for diagonalIndex in range(m + n - 1):
            level = []
            for i in range(min(diagonalIndex, m - 1), -1, -1):
                j = diagonalIndex - i
                if j >= n:
                    continue
                level.append(mat[i][j])
            if diagonalIndex % 2 == 0:
                ans.extend(level)
            else:
                ans.extend(level[::-1])

        return ans
