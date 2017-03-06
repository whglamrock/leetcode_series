'''
the top and most left elements of the grid are 1. then the lower right element is the sum the of
the above & left elements. The key is to think of iteration (the next always origins from the previous).
'''
class Solution(object):
    def uniquePaths(self, m, n):

        grid = [[1 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(1,m):
            for j in xrange(1,n):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]

        return grid[-1][-1]