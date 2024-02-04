from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        minSum = matrix[0]
        for i in range(1, m):
            nextMinSum = [0] * n
            for j in range(n):
                nextMinSum[j] = minSum[j] + matrix[i][j]
                if j > 0:
                    nextMinSum[j] = min(nextMinSum[j], minSum[j - 1] + matrix[i][j])
                if j < n - 1:
                    nextMinSum[j] = min(nextMinSum[j], minSum[j + 1] + matrix[i][j])
            minSum = nextMinSum

        return min(minSum)
