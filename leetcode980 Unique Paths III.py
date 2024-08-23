from typing import List


# There is no way to do any memoization to speed it up. brute force dfs. Time complexity is exponential: O(4 ^ (M*N)).
class Solution:
    def __init__(self):
        self.ans = 0
        self.emptyCells = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.emptyCells = 0
        start = [0, 0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = [i, j]
                    self.emptyCells += 1
                elif grid[i][j] == 0:
                    self.emptyCells += 1

        self.ans = 0
        self.dfs(grid, start[0], start[1])
        return self.ans

    def dfs(self, grid: List[List[int]], i: int, j: int):
        if grid[i][j] == 2:
            if self.emptyCells == 0:
                self.ans += 1
            return

        if self.emptyCells == 0:
            return

        # block the cell
        tmp = grid[i][j]
        grid[i][j] = -2
        self.emptyCells -= 1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[0]) or grid[ii][jj] < 0:
                continue
            self.dfs(grid, ii, jj)

        # recover the cell
        grid[i][j] = tmp
        self.emptyCells += 1
