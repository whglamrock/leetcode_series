from typing import List


# O(k * m * n) BFS solution.
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2

        indexToMinNumOfElimination = {}
        todo = {(0, 0, 0)}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        steps = 0
        while todo:
            nextTodo = set()
            for i, j, numOfElimination in todo:
                if i == m - 1 and j == n - 1:
                    return steps

                indexToMinNumOfElimination[(i, j)] = numOfElimination
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n:
                        continue
                    if grid[ii][jj] == 0:
                        if (ii, jj) in indexToMinNumOfElimination and indexToMinNumOfElimination[(ii, jj)] <= numOfElimination:
                            continue
                        indexToMinNumOfElimination[(ii, jj)] = numOfElimination
                        nextTodo.add((ii, jj, numOfElimination))
                    else:
                        # can't eliminate more
                        if numOfElimination == k:
                            continue
                        if (ii, jj) in indexToMinNumOfElimination and indexToMinNumOfElimination[(ii, jj)] <= numOfElimination + 1:
                            continue
                        indexToMinNumOfElimination[(ii, jj)] = numOfElimination + 1
                        nextTodo.add((ii, jj, numOfElimination + 1))

            steps += 1
            todo = nextTodo

        return -1
