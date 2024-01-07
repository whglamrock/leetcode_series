from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numOfIslands += 1

        return numOfIslands

    def dfs(self, grid: List[List[str]], i: int, j: int):
        if grid[i][j] == '0':
            return

        # sink the island
        grid[i][j] = '0'
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.dfs(grid, i - 1, j)
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)


print(Solution().numIslands([
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]))
