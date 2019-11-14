
# O(N^2) sinking the island solution; modifying the original grid

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        ans = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j)

        return ans

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        grid[i][j] = '0'
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.dfs(grid, i - 1, j)
        if i + 1 < m and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)
        if j + 1 < n and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)



print Solution().numIslands([
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
])
