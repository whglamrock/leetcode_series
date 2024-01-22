from typing import List

# there is no way you can any memoization to speed it up. Only plain old dfs
class Solution:
    def __init__(self):
        self.ans = 0
        self.emptyCells = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.emptyCells = 0
        start = (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.emptyCells += 1
                    start = (i, j)
                elif grid[i][j] == 0:
                    self.emptyCells += 1

        self.dfs(grid, start[0], start[1])
        return self.ans

    def dfs(self, grid: List[List[int]], i: int, j: int):
        if grid[i][j] == 2:
            if self.emptyCells == 0:
                self.ans += 1
            return

        if self.emptyCells <= 0:
            return

        # block this cell
        tmp = grid[i][j]
        grid[i][j] = -2
        self.emptyCells -= 1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and (
                    grid[ii][jj] == 0 or grid[ii][jj] == 2) and self.emptyCells >= 0:
                self.dfs(grid, ii, jj)

        # recover this cell
        grid[i][j] = tmp
        self.emptyCells += 1
