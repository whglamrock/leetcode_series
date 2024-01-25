# Google OA question.
# Solutions without using the built-in function can't be accepted by the motherfucking leetcode.
# so I force myself to use the 'join', 'split', which makes code short but ugly... waste of time.
# Stefan's answer: https://discuss.leetcode.com/topic/48566/short-o-mn-python
class Solution(object):
    def maxKilledEnemies(self, grid):

        if (not grid) or (not grid[0]):
            return 0

        row = [[-1] for i in range(len(grid))]
        col = [[-1] for i in range(len(grid[0]))]

        rowEnemy, colEnemy = [], []
        for i in range(len(grid)):  # record number of enemies a bomb can kill at different positions in each row
            breakdown = ''.join(grid[i]).split('W')
            new = []
            for item in breakdown:
                new.append(item.count('E'))
            rowEnemy.append(new)

        for j in range(len(grid[0])):  # record number of enemies a bomb can kill at different positions in each column
            breakdown = ''.join(grid[i][j] for i in range(len(grid))).split('W')
            new = []
            for item in breakdown:
                new.append(item.count('E'))
            colEnemy.append(new)

        for i in range(len(grid)):  # mark the position of walls by grid row, column.
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    row[i].append(j)
                    col[j].append(i)
                if i == len(grid) - 1:
                    col[j].append(len(grid))
            row[i].append(len(grid[0]))

        rowMap = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        colMap = [[0 for j in range(len(grid))] for i in range(len(grid[0]))]

        # mark the number of enemies can be killed with a bomb in each row with a bomb at different positions
        for i in range(len(row)):  # this i traverses the grid row (len(row) == len(grid))
            for j in range(len(row[i]) - 1):
                for k in range(row[i][j] + 1, row[i][j + 1]):
                    rowMap[i][k] = rowEnemy[i][j]

        # mark the number of enemies can be killed with a bomb in each column with a bomb at different positions
        for i in range(len(col)):  # this i traverses the grid column (len(col) == len(grid[0]))
            for j in range(len(col[i]) - 1):
                for k in range(col[i][j] + 1, col[i][j + 1]):
                    colMap[i][k] = colEnemy[i][j]

        # for every specific grid[i][j], adding the number of enemies can be killed in ith row and jth column.
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' and rowMap[i][j] + colMap[j][i] > ans:
                    ans = rowMap[i][j] + colMap[j][i]

        return ans


grid = [['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']]
print(Solution().maxKilledEnemies(grid))
