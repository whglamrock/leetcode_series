
class Solution(object):
    def countCornerRectangles(self, grid):

        m, n = len(grid), len(grid[0])
        ans = 0

        # count how many 1 pairs exist for a given column pair
        for j in xrange(n):
            for k in xrange(j + 1, n):
                count = 0
                for i in xrange(m):
                    if grid[i][j] == 1 and grid[i][k] == 1:
                        count += 1
                if count >= 2:
                    ans += count * (count - 1) / 2

        return ans



Sol = Solution()
grid = [[1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]]
print Sol.countCornerRectangles(grid)
