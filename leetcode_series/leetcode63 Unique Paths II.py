
# O(1) space solution, with modifying the obstacleGrid.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        if (not obstacleGrid) or (not obstacleGrid[0]):
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        i, j = 0, 1
        while i < m and obstacleGrid[i][0] != 1:
            obstacleGrid[i][0] = 1
            i += 1
        if i < m and obstacleGrid[i][0] == 1:
            while i < m:
                obstacleGrid[i][0] = 0
                i += 1
        while j < n and obstacleGrid[0][j] != 1:
            obstacleGrid[0][j] = 1
            j += 1
        if j < n and obstacleGrid[0][j] == 1:
            while j < n:
                obstacleGrid[0][j] = 0
                j += 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]



Sol = Solution()
grid = [[0,0,0,1,0],[0,0,1,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print Sol.uniquePathsWithObstacles(grid)



'''
# my original O(mn) time/space solution slow.
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0 for j in xrange(n)] for i in xrange(m)]
        i, j = 0, 0
        while i < m and obstacleGrid[i][0] != 1:
            grid[i][0] = 1
            i += 1
        while j < n and obstacleGrid[0][j] != 1:
            grid[0][j] = 1
            j += 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] != 1:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0

        return grid[-1][-1]
'''
