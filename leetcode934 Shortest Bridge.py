from copy import deepcopy
from typing import List

# DFS + BFS O(N * N) solution
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        gridCopy = deepcopy(grid)

        island1Index = set()
        island2Index = set()
        for i in range(n):
            for j in range(n):
                if gridCopy[i][j] == 0:
                    continue
                if not island1Index:
                    self.dfsSinkTheIsland(gridCopy, island1Index, i, j)
                else:
                    self.dfsSinkTheIsland(gridCopy, island2Index, i, j)
                break

        todo = set()
        for i, j in island1Index:
            if self.isWaterFront(grid, i, j):
                todo.add((i, j))

        shortestBridge = 0
        while todo:
            nextTodo = set()
            for i, j in todo:
                if i - 1 >= 0:
                    if (i - 1, j) in island2Index:
                        return shortestBridge
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                        nextTodo.add((i - 1, j))
                if i + 1 < n:
                    if (i + 1, j) in island2Index:
                        return shortestBridge
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                        nextTodo.add((i + 1, j))
                if j - 1 >= 0:
                    if (i, j - 1) in island2Index:
                        return shortestBridge
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                        nextTodo.add((i, j - 1))
                if j + 1 < n:
                    if (i, j + 1) in island2Index:
                        return shortestBridge
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                        nextTodo.add((i, j + 1))
            todo = nextTodo
            shortestBridge += 1

        return shortestBridge

    def dfsSinkTheIsland(self, grid: List[List[int]], islandIndexes: set, i: int, j: int):
        grid[i][j] = 0
        islandIndexes.add((i, j))
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        n = len(grid)
        for deltaI, deltaJ in directions:
            ii = i + deltaI
            jj = j + deltaJ
            if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 1:
                self.dfsSinkTheIsland(grid, islandIndexes, ii, jj)

    def isWaterFront(self, grid: List[List[int]], i: int, j: int) -> bool:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        n = len(grid)
        for deltaI, deltaJ in directions:
            ii = i + deltaI
            jj = j + deltaJ
            if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0:
                return True
        return False


print(Solution().shortestBridge([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]]))
print(Solution().shortestBridge([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]))
