
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        return self.bfs(grid, 0, 0)

    def bfs(self, grid, x, y):
        todo = set()
        todo.add((x, y))
        path = 0
        n = len(grid)

        while todo:

            next_todo = set()
            for i, j in todo:
                if i == j == n - 1:
                    return path + 1
                grid[i][j] = 2

                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    next_todo.add((i - 1, j))
                    grid[i - 1][j] = 2
                if i + 1 < n and grid[i + 1][j] == 0:
                    next_todo.add((i + 1, j))
                    grid[i + 1][j] = 2
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    next_todo.add((i, j - 1))
                    grid[i][j - 1] = 2
                if j + 1 < n and grid[i][j + 1] == 0:
                    next_todo.add((i, j + 1))
                    grid[i][j + 1] = 2
                if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == 0:
                    next_todo.add((i - 1, j - 1))
                    grid[i - 1][j - 1] = 2
                if i - 1 >= 0 and j + 1 < n and grid[i - 1][j + 1] == 0:
                    next_todo.add((i - 1, j + 1))
                    grid[i - 1][j + 1] = 2
                if i + 1 < n and j - 1 >= 0 and grid[i + 1][j - 1] == 0:
                    next_todo.add((i + 1, j - 1))
                    grid[i + 1][j - 1] = 2
                if i + 1 < n and j + 1 < n and grid[i + 1][j + 1] == 0:
                    next_todo.add((i + 1, j + 1))
                    grid[i + 1][j + 1] = 2

            path += 1
            todo = next_todo

        return -1


