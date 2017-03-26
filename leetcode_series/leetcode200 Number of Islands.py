
'''
sink the island solution, modifying the original grid.
once find one breakthrough point, through recursion find all connected '1's and make them 0,
then visiting other grid[i][j]s, no duplicate '1's will be counted.
O(N^2) time.
'''

class Solution(object):
    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0

        count = 0
        self.grid = grid

        def helper(i, j):
            # 'sink' the island
            self.grid[i][j] = '0'
            if j > 0 and self.grid[i][j - 1] == '1':
                helper(i, j - 1)
            if j < len(self.grid[0]) - 1 and grid[i][j + 1] == '1':
                helper(i, j + 1)
            if i > 0 and self.grid[i - 1][j] == '1':
                helper(i - 1, j)
            if i < len(self.grid) - 1 and self.grid[i + 1][j] == '1':
                helper(i + 1, j)

        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    count += 1
                    helper(i, j)

        return count



grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
Sol = Solution()
print Sol.numIslands(grid)



'''
# iterative version

class Solution(object):
    def numIslands(self, grid):

        if (not grid) or (not grid[0]):
            return 0

        numofislands = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                todo = []
                if grid[i][j] == '1':
                    numofislands += 1
                    todo.append([i,j])
                while todo:
                    #print todo
                    x, y = todo.pop()
                    grid[x][y] = '0'
                    if x + 1 < len(grid) and grid[x + 1][y] == '1':
                        todo.append([x + 1, y])
                    if y + 1 < len(grid[0]) and grid[x][y + 1] == '1':
                        todo.append([x, y + 1])
                    if x - 1 >= 0 and grid[x - 1][y] == '1':
                        todo.append([x - 1, y])
                    if y - 1 >= 0 and grid[x][y - 1] == '1':
                        todo.append([x, y - 1])

        return numofislands
'''