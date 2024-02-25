from typing import List

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        startI, startJ = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    startI, startJ = i, j
                    break

        todo = {(startI, startJ)}
        distance = 0
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while todo:
            nextTodo = set()
            for i, j in todo:
                if grid[i][j] == '#':
                    return distance
                visited.add((i, j))
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] in 'O#' and (ii, jj) not in visited:
                        nextTodo.add((ii, jj))
            todo = nextTodo
            distance += 1

        return -1
