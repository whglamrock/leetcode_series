from typing import List


# We have to use backtracking (i.e., marking grid[i][j] = 0 for dfs then changing it back to its original value).
# Using a path set to store the visited indexes will cause TLE in the stupid leetcode
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, self.dfs(grid, i, j))

        return ans

    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        tmp = grid[i][j]
        grid[i][j] = 0

        maxAdditionalGold = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(grid), len(grid[0])
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if ii < 0 or ii >= m or jj < 0 or jj >= n:
                continue
            if grid[ii][jj]:
                maxAdditionalGold = max(maxAdditionalGold, self.dfs(grid, ii, jj))

        grid[i][j] = tmp
        return maxAdditionalGold + tmp
