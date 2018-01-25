
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):

        grid = [[N for j in xrange(N)] for i in xrange(N)]
        for mine in mines:
            grid[mine[0]][mine[1]] = 0

        # longest stretch in left direction
        for i in xrange(N):
            l = 0
            for j in xrange(N):
                l = l + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], l)
        # longest stretch in right direction
        for i in xrange(N):
            r = 0
            for j in xrange(N - 1, -1, -1):
                r = r + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], r)
        # longest stretch in up direction
        for j in xrange(N):
            u = 0
            for i in xrange(N):
                u = u + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], u)
        # longest stretch in down direction
        for j in xrange(N):
            d = 0
            for i in xrange(N - 1, -1, -1):
                d = d + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], d)

        ans = 0
        for i in xrange(N):
            for j in xrange(N):
                ans = max(ans, grid[i][j])
        return ans



Sol = Solution()
mines = [[4, 2]]
print Sol.orderOfLargestPlusSign(5, mines)

