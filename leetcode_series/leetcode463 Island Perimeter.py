
# See my explanation from: https://discuss.leetcode.com/topic/76791/python-o-mn-time-o-1-space-easy-to-understand-solution

class Solution(object):
    def islandPerimeter(self, grid):

        if not grid or not grid[0]:
            return 0

        perimeter = 0
        for i in xrange(len(grid)):
            count = 0
            for j in xrange(len(grid[0])):
                if (j == 0 and grid[i][j] == 1) or (j >= 1 and grid[i][j] == 1 and grid[i][j - 1] == 0):
                    count += 1
            perimeter += count * 2

        for j in xrange(len(grid[0])):
            count = 0
            for i in xrange(len(grid)):
                if (i == 0 and grid[i][j] == 1) or (i >= 1 and grid[i][j] == 1 and grid[i - 1][j] == 0):
                    count += 1
            perimeter += count * 2

        return perimeter