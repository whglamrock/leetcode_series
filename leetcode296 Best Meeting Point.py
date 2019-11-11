
# The idea is we need to place the meeting point between/on the median point of the x & y coordinates.
    # it isn't hard to prove that is the optimal meeting point

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = [], []
        m, n = len(grid), len(grid[0])

        # Because we are looping through the whole grid, row & col lists are sorted
        # Each row/col can have multiple people so we use median (not avg) as best meeting point
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    rows.append(i)
        for j in xrange(n):
            for i in xrange(m):
                if grid[i][j] == 1:
                    cols.append(j)

        # x, y is the idea meeting point
        x, y = rows[len(rows) / 2], cols[len(cols) / 2]
        ans = 0
        for row in rows:
            ans += abs(row - x)
        for col in cols:
            ans += abs(col - y)

        return ans



print Solution().minTotalDistance([
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]])