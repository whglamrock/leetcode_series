
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):

        # at first, set each position value to N instead of 1,
        #   because we need to get the min(grid[i][j], leg length)
        grid = [[N for j in xrange(N)] for i in xrange(N)]
        for mine in mines:
            x, y = mine[0], mine[1]
            grid[x][y] = 0

        # legs are on the left:
        for i in xrange(N):
            r = 0
            for j in xrange(N):
                r = r + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], r)

        # legs are on the right:
        for i in xrange(N):
            r = 0
            for j in xrange(N - 1, -1, -1):
                r = r + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], r)

        # legs are above:
        for j in xrange(N):
            r = 0
            for i in xrange(N):
                r = r + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], r)

        # legs are under:
        for j in xrange(N):
            r = 0
            for i in xrange(N - 1, -1, -1):
                r = r + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], r)

        ans = 0
        for i in xrange(N):
            for j in xrange(N):
                ans = max(ans, grid[i][j])

        return ans



Sol = Solution()
mines = [[4, 2]]
print Sol.orderOfLargestPlusSign(5, mines)

