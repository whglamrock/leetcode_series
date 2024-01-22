from typing import List

# O(k * m * n) solution with BFS. we have to use BFS instead of DFS to avoid TLE.
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        steps = 0
        todo = [[0, 0, k]]
        # because we are using BFS to find the shortest path, it's safe to not visit
        # the same cell if if we have eliminated the same amount of obstacles
        visited = {0, 0, k}

        while todo:
            nextTodo = []
            for i, j, k in todo:
                if i == m - 1 and j == n - 1:
                    return steps
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < m and 0 <= jj < n:
                        kk = k if grid[ii][jj] == 0 else k - 1
                        if kk >= 0 and (ii, jj, kk) not in visited:
                            nextTodo.append([ii, jj, kk])
                            visited.add((ii, jj, kk))
            todo = nextTodo
            steps += 1

        return -1
