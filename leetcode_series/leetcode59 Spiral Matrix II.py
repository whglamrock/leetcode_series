class Solution(object):
    def generateMatrix(self, n):

        if n <= 0:
            return []
        if n == 1:
            return [[1]]
        i, j = 0, 0
        counter = 1
        direction = 'right'
        grid = [[0 for x in xrange(n)] for y in xrange(n)]

        while counter < n*n+1:
            grid[i][j] = counter
            if direction == 'right':
                j += 1
                if grid[i][j] != 0:
                    j -= 1
                    i += 1
                    direction = 'down'
                if j == n-1:
                    direction = 'down'
            elif direction == 'down':
                i += 1
                if grid[i][j] != 0:
                    i -= 1
                    j -= 1
                    direction = 'left'
                if i == n-1:
                    direction = 'left'
            elif direction == 'left':
                j -= 1
                if grid[i][j] != 0:
                    j += 1
                    i -= 1
                    direction = 'up'
                if j == 0:
                    direction = 'up'
            else:
                i -= 1
                if grid[i][j] != 0:
                    i += 1
                    j += 1
                    direction = 'right'
            counter += 1

        return grid

Sol = Solution()
print Sol.generateMatrix(5)

