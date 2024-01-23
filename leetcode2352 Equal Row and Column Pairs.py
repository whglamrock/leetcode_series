from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowStrCount, colStrCount = defaultdict(int), defaultdict(int)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            row = []
            for j in range(n):
                row.append(str(grid[i][j]))
            rowStrCount[','.join(row)] += 1
        for j in range(n):
            col = []
            for i in range(m):
                col.append(str(grid[i][j]))
            colStrCount[','.join(col)] += 1

        ans = 0
        for rowStr in rowStrCount:
            if rowStr in colStrCount:
                ans += rowStrCount[rowStr] * colStrCount[rowStr]
        return ans
