
# the idea:
    # 1) do BFS starting from every building;
    # 2) after all BFSes, grid[i][j] == len(buildings) means this cell can access all buildings

from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid and not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        buildings = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    buildings.append((i, j, 0))
                # this is for the trick later in bfs
                grid[i][j] = -grid[i][j]

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distances = [[0 for j in xrange(n)] for i in xrange(m)]

        for k in xrange(len(buildings)):
            self.bfs(grid, buildings[k], k, distances, dirs)

        shortestDist = -1
        for i in xrange(m):
            for j in xrange(n):
                # this point is reachable to all buildings
                if grid[i][j] == len(buildings):
                    if shortestDist == -1:
                        shortestDist = distances[i][j]
                    else:
                        shortestDist = min(shortestDist, distances[i][j])

        return shortestDist

    def bfs(self, grid, root, k, distances, dirs):
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append(root)

        while queue:
            i, j, dist = queue.popleft()
            # we are doing BFS, so once i, j has been reached it's for sure the shortest distance;
            # Also setting "grid[i][j] == k + 1" makes we don't double visit
            distances[i][j] += dist
            for h, v in dirs:
                x, y = i + h, j + v
                # grid[x][y] == k means it's reachable till last building
                if 0 <= x < m and 0 <= y < n and grid[x][y] == k:
                    queue.append((x, y, dist + 1))
                    # remember to update the grid[i][j] here
                    grid[x][y] = k + 1