
# The idea is we need to place the meeting point between/on the median point of the x & y coordinates.
    # it isn't hard to prove that is the optimal meeting point

class Solution(object):
    def minTotalDistance(self, grid):

        if (not grid) or (not grid[0]):
            return 0

        # Because we are looping through the whole grid, row & col lists are sorted
        # Each row/col can have multiple people but it's fine because we use median (not avg) as best meeting point
        row, col = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)

        for j in xrange(len(grid[0])):
            for i in xrange(len(grid)):
                if grid[i][j] == 1:
                    col.append(j)

        midRow = row[len(row) / 2]
        midCol = col[len(col) / 2]
        ans = 0
        for y in row:
            ans += abs(y - midRow)
        for x in col:
            ans += abs(x - midCol)

        return ans