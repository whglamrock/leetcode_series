from typing import List

# Think about doing dfs in a graph instead of a grid. The most straightforward way you detect a cycle is using
# dfs + a visited set. 2 nodes(cell) are connected only if they are adjacent and have the same character.
class Solution:
    def __init__(self):
        self.visited = set()

    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        self.visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in self.visited:
                    continue
                currChar = grid[i][j]
                if self.dfs(grid, i, j, -1, -1, currChar):
                    return True

        return False

    def dfs(self, grid: List[List[str]], i: int, j: int, lastI: int, lastJ: int, currChar: str) -> bool:
        if (i, j) in self.visited:
            return True
        self.visited.add((i, j))

        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if ii < 0 or ii >= m or jj < 0 or jj >= n or (ii == lastI and jj == lastJ) or grid[ii][jj] != currChar:
                continue
            if self.dfs(grid, ii, jj, i, j, currChar):
                return True

        return False
