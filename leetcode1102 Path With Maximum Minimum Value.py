from heapq import *
from typing import List

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [[-grid[0][0], 0, 0]]
        indexToMaxPathScore = {}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while pq:
            score, i, j = heappop(pq)
            score = -score
            if i == m - 1 and j == n - 1:
                return score
            if (i, j) not in indexToMaxPathScore or indexToMaxPathScore[(i, j)] < score:
                indexToMaxPathScore[(i, j)] = score
            for deltaI, deltaJ in directions:
                ii, jj = i + deltaI, j + deltaJ
                if 0 <= ii < m and 0 <= jj < n:
                    newScore = min(score, grid[ii][jj])
                    if (ii, jj) not in indexToMaxPathScore or indexToMaxPathScore[(ii, jj)] < newScore:
                        indexToMaxPathScore[(ii, jj)] = newScore
                        heappush(pq, [-newScore, ii, jj])

        return indexToMaxPathScore[(m - 1, n - 1)]


print(Solution().maximumMinimumPath([
    [5, 4, 5],
    [1, 2, 6],
    [7, 4, 6]]))
print(Solution().maximumMinimumPath([
    [2, 2, 1, 2, 2, 2],
    [1, 2, 2, 2, 1, 2]]))
print(Solution().maximumMinimumPath([
    [3, 4, 6, 3, 4],
    [0, 2, 1, 1, 7],
    [8, 8, 3, 2, 7],
    [3, 2, 4, 9, 8],
    [4, 1, 2, 0, 0],
    [4, 6, 5, 4, 3]]))
