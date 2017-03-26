
class Solution(object):
    def minPathSum(self, grid):
        
        ans = [[0 for x in xrange(len(grid[0]))] for y in xrange(len(grid))]
        for k in xrange(len(grid)):
            if k == 0:
                ans[k][0] = grid[k][0]
            else:
                ans[k][0] = ans[k-1][0]+grid[k][0]
        for l in xrange(len(grid[0])):
            if l == 0:
                ans[0][l] = grid[0][l]
            else:
                ans[0][l] = ans[0][l-1]+grid[0][l]

        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                ans[i][j] = min(ans[i][j-1],ans[i-1][j]) + grid[i][j]

        return ans[-1][-1]