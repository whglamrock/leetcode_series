from typing import List

# any island that contains a cell on the edge is considered not "closed".
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and self.isTheIslandClosed(grid, i, j):
                    ans += 1

        return ans

    def isTheIslandClosed(self, grid: List[List[int]], x: int, y: int) -> bool:
        todo = {(x, y)}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(grid), len(grid[0])
        islandClosed = True
        while todo:
            nextTodo = set()
            for i, j in todo:
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    islandClosed = False
                # sink the island
                grid[i][j] = 2
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 0:
                        nextTodo.add((ii, jj))
            todo = nextTodo

        return islandClosed
