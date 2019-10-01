
# A hard level question. It's impractical to use the DP approach because we have to store the state of whole grid in
    # each loop. A recursive DFS solution is easier and more practical for interview

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = self.dfs(0, 0, 0, 0, grid, {})
        return ans if ans > 0 else 0

    # find two paths (can overlap) that have max sum of cherries
    def dfs(self, x1, y1, x2, y2, grid, memo):
        n = len(grid)

        # check if we reached bottom right corner; (x1, y1), (x2, y2) will reach bottom right at the same time
        if x1 == n - 1 and y1 == n - 1:
            return grid[-1][-1] if grid[-1][-1] >= 0 else -2147483647

        if x1 >= n or y1 >= n or x2 >= n or y2 >= n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -2147483647

        if (x1, y1, x2, y2) in memo:
            return memo[(x1, y1, x2, y2)]

        if x1 == x2 and y1 == y2:
            cherries = grid[x1][y1]
        else:
            cherries = grid[x1][y1] + grid[x2][y2]

        res = cherries + max(
            self.dfs(x1 + 1, y1, x2 + 1, y2, grid, memo),
            self.dfs(x1 + 1, y1, x2, y2 + 1, grid, memo),
            self.dfs(x1, y1 + 1, x2 + 1, y2, grid, memo),
            self.dfs(x1, y1 + 1, x2, y2 + 1, grid, memo)
        )

        memo[(x1, y1, x2, y2)] = res
        return res