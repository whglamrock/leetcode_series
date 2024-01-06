from heapq import *
from typing import List

# dijkstra's algorithm make sure when (i, j) is first reached, it's always the shortest path.
# O(n^2 * log(n^2)) time solution.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # when each (i, j) is visited, we store the smallest (highest elevation seen in the path)
        indexToSmallestHighestInPath = {}
        # use pq to always search from the lowest elevation
        pq = [[grid[-1][-1], n - 1, n - 1]]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while pq:
            currHighest, i, j = heappop(pq)
            if (i, j) not in indexToSmallestHighestInPath or indexToSmallestHighestInPath[(i, j)] > currHighest:
                indexToSmallestHighestInPath[(i, j)] = currHighest
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < n and 0 <= jj < n:
                        if (ii, jj) == (0, 0):
                            return max(currHighest, grid[0][0])
                        # only add it to heapq if the next index is not visited or has a bigger smallest elevation in path
                        if (ii, jj) not in indexToSmallestHighestInPath or indexToSmallestHighestInPath[(ii, jj)] > currHighest:
                            heappush(pq, [max(grid[ii][jj], currHighest), ii, jj])

        return indexToSmallestHighestInPath[(0, 0)]



