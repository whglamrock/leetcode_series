# Google OA question.
# Solutions without using the built-in function can't be accepted by the motherfuncking leetcode.
# so I force myself to use the 'join', 'split', which makes code short but ugly... waste of time.
# Stefan's answer: https://discuss.leetcode.com/topic/48566/short-o-mn-python
class Solution(object):
    def maxKilledEnemies(self, grid):

        if (not grid) or (not grid[0]):
            return 0

        row = [[-1] for i in xrange(len(grid))]
        col = [[-1] for i in xrange(len(grid[0]))]

        rowenemy, colenemy = [], []
        for i in xrange(len(grid)):   # record number of enemies a bomb can kill at different positions in each row
            breakdown = ''.join(grid[i]).split('W')
            new = []
            for item in breakdown:
                new.append(item.count('E'))
            rowenemy.append(new)

        for j in xrange(len(grid[0])):  # record number of enemies a bomb can kill at different positions in each column
            breakdown = ''.join(grid[i][j] for i in xrange(len(grid))).split('W')
            new = []
            for item in breakdown:
                new.append(item.count('E'))
            colenemy.append(new)

        for i in xrange(len(grid)): # mark the position of walls by grid row, column.
            for j in xrange(len(grid[0])):
                if grid[i][j] == 'W':
                    row[i].append(j)
                    col[j].append(i)
                if i == len(grid)-1:
                    col[j].append(len(grid))
            row[i].append(len(grid[0]))

        rowmap = [[0 for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        colmap = [[0 for j in xrange(len(grid))] for i in xrange(len(grid[0]))]

        # mark the number of enemies can be killed with a bomb in each row with a bomb at different positions
        for i in xrange(len(row)):  # this i traverses the grid row (len(row) == len(grid))
            for j in xrange(len(row[i])-1):
                for k in xrange(row[i][j]+1, row[i][j+1]):
                    rowmap[i][k] = rowenemy[i][j]

        # mark the number of enemies can be killed with a bomb in each column with a bomb at different positions
        for i in xrange(len(col)):  # this i traverses the grid column (len(col) == len(grid[0]))
            for j in xrange(len(col[i])-1):
                for k in xrange(col[i][j]+1, col[i][j+1]):
                    colmap[i][k] = colenemy[i][j]

        # for every specific grid[i][j], adding the number of enemies can be killed in ith row and jth column.
        ans = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '0' and rowmap[i][j]+colmap[j][i] > ans:
                    ans = rowmap[i][j]+colmap[j][i]

        return ans


Sol = Solution()
grid = [['0','E','0','0'],['E','0','W','E'],['0','E','0','0']]
print Sol.maxKilledEnemies(grid)


'''
# Stefan's answer with built-in functions:
class Solution(object):
    def maxKilledEnemies(self, grid):
        def hits(grid):
            return [[h
                    for block in ''.join(row).split('W')
                    for h in [block.count('E')] * len(block) + [0]]
                    for row in grid]
        rowhits = hits(grid)
        colhits = zip(*hits(zip(*grid)))
        return max([rh + ch
                    for row in zip(grid, rowhits, colhits)
                    for cell, rh, ch in zip(*row)
                    if cell == '0'] or [0])
'''




