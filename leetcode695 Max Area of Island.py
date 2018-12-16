
from collections import deque

# again, sink the island idea
class Solution(object):
    def maxAreaOfIsland(self, grid):

        maxArea = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.bfs(grid, i, j)
                    maxArea = max(maxArea, area)

        return maxArea

    def bfs(self, grid, i, j):
        grid[i][j] = 0
        todo = deque()
        todo.append([i, j])
        area = 0

        while todo:
            x, y = todo.popleft()
            area += 1
            if x - 1 >= 0 and grid[x - 1][y] == 1:
                todo.append([x - 1, y])
                grid[x - 1][y] = 0
            if x + 1 < len(grid) and grid[x + 1][y] == 1:
                todo.append([x + 1, y])
                grid[x + 1][y] = 0
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                todo.append([x, y - 1])
                grid[x][y - 1] = 0
            if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
                todo.append([x, y + 1])
                grid[x][y + 1] = 0
        return area


