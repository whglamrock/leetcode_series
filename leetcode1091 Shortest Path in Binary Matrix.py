from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        m, n = len(grid), len(grid[0])
        todo = {(0, 0)}
        dist = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        visited = set()
        while todo:
            nextTodo = set()
            for i, j in todo:
                if i == m - 1 and j == n - 1:
                    return dist + 1
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n:
                        continue
                    if (ii, jj) not in visited and grid[ii][jj] == 0:
                        nextTodo.add((ii, jj))
            todo = nextTodo
            dist += 1

        return -1
