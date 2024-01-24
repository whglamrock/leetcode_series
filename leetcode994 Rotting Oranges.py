from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        todo = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    todo.add((i, j))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        minutes = 0
        while todo:
            nextTodo = set()
            for i, j in todo:
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        nextTodo.add((ii, jj))
                        grid[ii][jj] = 2
            todo = nextTodo
            if todo:
                minutes += 1

        existsAnyFreshOrange = False
        for row in grid:
            for cell in row:
                if cell == 1:
                    existsAnyFreshOrange = True
                    break

        return minutes if not existsAnyFreshOrange else -1
