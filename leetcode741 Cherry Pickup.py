
class Solution(object):
    def cherryPickup(self, grid):

        memo = {}
        res = self.dfs(0, 0, 0, 0, grid, memo)
        return res if res > 0 else 0

    def dfs(self, x1, y1, x2, y2, grid, memo):
        n = len(grid)
        # check if we reached bottom right corner; (x1, y1), (x2, y2) will reach bottom right at the same time
        if x1 == n - 1 and y1 == n - 1:
            return grid[x1][y1] if grid[x1][y1] != -1 else -2147483648

        # out of the grid and thorn check
        if x1 == n or y1 == n or x2 == n or y2 == n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -2147483648

        # memorization check
        if (x1, y1, x2, y2) in memo:
            return memo[(x1, y1, x2, y2)]

        # pick your cherries
        if x1 == x2 and y1 == y2:
            cherries = grid[x1][y1]
        else:
            cherries = grid[x1][y1] + grid[x2][y2]

        res = cherries + max(
            self.dfs(x1 + 1, y1, x2 + 1, y2, grid, memo),  # right, right
            self.dfs(x1, y1 + 1, x2, y2 + 1, grid, memo),  # down, down
            self.dfs(x1 + 1, y1, x2, y2 + 1, grid, memo),  # right, down
            self.dfs(x1, y1 + 1, x2 + 1, y2, grid, memo)  # down, right
        )

        memo[(x1, y1, x2, y2)] = res
        return res