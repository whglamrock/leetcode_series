
'''
sink the island solution, modifying the original grid.
once find one breakthrough point, through recursion find all connected '1's and make them 0,
then visiting other grid[i][j]s, no duplicate '1's will be counted.
O(N^2) time.
'''

from collections import deque

class Solution(object):
    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0
        numofisland = 0
        m, n = len(grid), len(grid[0])

        for i in xrange(m):
            for j in xrange(n):
                 if grid[i][j] == '1':
                     numofisland += 1
                     todo = deque()
                     todo.append((i, j))
                     while todo:
                         x, y = todo.popleft()
                         grid[x][y] = '0'
                         # put the '1' cell to '0' in each if condition to limit the number of
                         #   append operations
                         if x > 0 and grid[x - 1][y] == '1':
                             todo.append((x - 1, y))
                             grid[x - 1][y] = '0'
                         if x < m - 1 and grid[x + 1][y] == '1':
                             todo.append((x + 1, y))
                             grid[x + 1][y] = '0'
                         if y > 0 and grid[x][y - 1] == '1':
                             todo.append((x, y - 1))
                             grid[x][y - 1] = '0'
                         if y < n - 1 and grid[x][y + 1] == '1':
                             todo.append((x, y + 1))
                             grid[x][y + 1] = '0'

        return numofisland



grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
Sol = Solution()
print Sol.numIslands(grid)


