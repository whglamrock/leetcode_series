
from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):

        if not heightMap or len(heightMap[0]) == 0:
            return 0

        pq = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            visited[i][0], visited[i][-1] = True, True
            heappush(pq, [heightMap[i][0], (i, 0)])
            heappush(pq, [heightMap[i][-1], (i, n - 1)])


        for j in xrange(1, n - 1):
            visited[0][j], visited[-1][j] = True, True
            heappush(pq, [heightMap[0][j], (0, j)])
            heappush(pq, [heightMap[-1][j], (m - 1, j)])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        while pq:
            cell = heappop(pq)
            for x, y in dirs:
                row, col = cell[1][0] + x, cell[1][1] + y
                if 0 <= row < m and 0 <= col < n and (not visited[row][col]):
                    visited[row][col] = True
                    res += max(0, cell[0] - heightMap[row][col])
                    heappush(pq, [max(cell[0], heightMap[row][col]), (row, col)])

        return res