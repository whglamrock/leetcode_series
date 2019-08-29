
# use a 3 * 3 matrix to represent each grid

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        grid = self.convertGrid(grid)

        ans = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 1
                    self.dfs(grid, i, j)

        return ans

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            self.dfs(grid, i - 1, j)
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            self.dfs(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            self.dfs(grid, i, j - 1)
        if j + 1 < len(grid) and grid[i][j + 1] == 1:
            self.dfs(grid, i, j + 1)

    def convertGrid(self, grid):
        n = len(grid)
        newGrid = [[1 for j in xrange(n * 3)]  for i in xrange(n * 3)]

        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == ' ':
                    continue
                elif grid[i][j] == '/':
                    newGrid[i * 3 + 0][j * 3 + 2] = 0
                    newGrid[i * 3 + 1][j * 3 + 1] = 0
                    newGrid[i * 3 + 2][j * 3 + 0] = 0
                else:
                    newGrid[i * 3 + 0][j * 3 + 0] = 0
                    newGrid[i * 3 + 1][j * 3 + 1] = 0
                    newGrid[i * 3 + 2][j * 3 + 2] = 0

        return newGrid


