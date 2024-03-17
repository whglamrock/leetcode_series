from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea = max(maxArea, self.sinkTheIsland(grid, i, j))

        return maxArea

    def sinkTheIsland(self, grid: List[List[int]], x: int, y: int) -> int:
        area = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(grid), len(grid[0])
        todo = {(x, y)}
        while todo:
            nextTodo = set()
            for i, j in todo:
                area += 1
                grid[i][j] = 0
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n or grid[ii][jj] == 0:
                        continue
                    nextTodo.add((ii, jj))
            todo = nextTodo

        return area
