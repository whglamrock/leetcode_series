from collections import defaultdict
from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        indexToOnes, indexToZeros = defaultdict(int), defaultdict(int)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            numOfOnes, numOfZeros = 0, 0
            for j in range(n):
                if grid[i][j] == 1:
                    numOfOnes += 1
                else:
                    numOfZeros += 1
            for j in range(n):
                indexToOnes[(i, j)] += numOfOnes
                indexToZeros[(i, j)] += numOfZeros
        for j in range(n):
            numOfOnes, numOfZeros = 0, 0
            for i in range(m):
                if grid[i][j] == 1:
                    numOfOnes += 1
                else:
                    numOfZeros += 1
            for i in range(m):
                indexToOnes[(i, j)] += numOfOnes
                indexToZeros[(i, j)] += numOfZeros

        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = indexToOnes[(i, j)] - indexToZeros[(i, j)]
        return ans
