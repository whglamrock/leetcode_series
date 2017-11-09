
# try to solve this problem in one-dimensional number axis!
# for every hard question, we need to unmask the knowledge behind it and transfer it
# into normal, common math/algorithm question.

class Solution(object):
    def minTotalDistance(self, grid):

        if (not grid) or (not grid[0]):
            return 0

        row, col = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)

        for j in xrange(len(grid[0])):
            for i in xrange(len(grid)):
                if grid[i][j] == 1:
                    col.append(j)

        # we take the median because we don't need to worry about the duplicates in grid
        # grid[i][j] = 1 means for only 1 person, even there are more than one people on
        # the same spot, distance will only calculated once.
        midrow = row[len(row) / 2]
        midcol = col[len(col) / 2]
        ans = 0
        for y in row:
            ans += abs(y - midrow)
        for x in col:
            ans += abs(x - midcol)

        return ans