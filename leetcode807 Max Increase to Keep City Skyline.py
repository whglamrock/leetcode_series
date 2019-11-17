
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        verticalSkyline = [0] * m
        horizontalSkyline = [0] * n

        for i in xrange(m):
            for j in xrange(n):
                verticalSkyline[i] = max(verticalSkyline[i], grid[i][j])
                horizontalSkyline[j] = max(horizontalSkyline[j], grid[i][j])

        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                ans += min(verticalSkyline[i], horizontalSkyline[j]) - grid[i][j]

        return ans