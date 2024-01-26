from heapq import *
from typing import List

# dijkstra's algorithm make sure when (i, j) is first reached, it's always the shortest path.
# O(n^2 * log(n^2)) time solution.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # stores the min (max elevation of the route progressed so far) of all routes passing through (i, j)
        indexToMaxElevation = {(0, 0): grid[0][0]}
        pq = [[grid[0][0], 0, 0]]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while pq:
            currHeight, i, j = heappop(pq)
            if i == j == n - 1:
                return indexToMaxElevation[(i, j)]
            for deltaI, deltaJ in directions:
                ii, jj = i + deltaI, j + deltaJ
                if 0 <= ii < n and 0 <= jj < n:
                    newHeight = max(currHeight, grid[ii][jj])
                    if (ii, jj) not in indexToMaxElevation or indexToMaxElevation[(ii, jj)] > newHeight:
                        indexToMaxElevation[(ii, jj)] = newHeight
                        heappush(pq, [newHeight, ii, jj])

        # useless, just to avoid syntax warning
        return 0
