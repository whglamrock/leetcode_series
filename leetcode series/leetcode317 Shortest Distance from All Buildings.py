
# the idea: 1) do BFS starting from every building;
#           2) after all BFSes, grid[i][j] == len(buildings) means this cell can access all buildings

from collections import deque

class Solution(object):
    def shortestDistance(self, grid):

        if not grid or len(grid[0]) == 0:
            return 0
        self.grid = grid
        m, n = len(grid), len(grid[0])
        buildings = []

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    buildings.append((i, j, 0))
                # put them negative so we can use the trick for BFS
                grid[i][j] = -grid[i][j]    # available cells (zeroes) won't be affected

        # the element of dist is the distance sum from once position to all buildings
        self.dist = [[0 for j in xrange(n)] for i in xrange(m)]
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for k in xrange(len(buildings)):
            self.bfs(buildings[k], k, m, n)
        shortestdist = -1

        for i in xrange(m):
            for j in xrange(n):
                if self.grid[i][j] == len(buildings):
                    if shortestdist == -1:
                        shortestdist = self.dist[i][j]
                    else:
                        shortestdist = min(shortestdist, self.dist[i][j])

        return shortestdist

    # root is the position of building
    def bfs(self, root, k, m, n):

        q = deque()
        q.append(root)
        while q:
            row, col, currdist = q.popleft()
            # once grid[row][col] is walked on, the path is for sure the shortest and the corresponding
            #   shortest distance from building k to this point is confirmed, and "self.grid[r][c] == k"
            #   makes sure this cell will only be walked on once from a specific building
            self.dist[row][col] += currdist
            for x, y in self.dirs:
                r, c = row + x, col + y
                if 0 <= r < m and 0 <= c < n and self.grid[r][c] == k:
                    self.grid[r][c] = k + 1
                    q.append((r, c, currdist + 1))