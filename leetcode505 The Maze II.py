from heapq import *
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        pq = [[0, start[0], start[1]]]
        indexToMinDist = {}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while pq:
            distance, i, j = heappop(pq)
            if i == destination[0] and j == destination[1]:
                return distance
            if (i, j) in indexToMinDist and indexToMinDist[(i, j)] < distance:
                continue
            indexToMinDist[(i, j)] = distance

            for deltaI, deltaJ in directions:
                ii, jj = i + deltaI, j + deltaJ
                nextDistance = distance
                while 0 <= ii < m and 0 <= jj < n and maze[ii][jj] == 0:
                    ii += deltaI
                    jj += deltaJ
                    nextDistance += 1
                ii -= deltaI
                jj -= deltaJ
                if (ii, jj) in indexToMinDist and indexToMinDist[(ii, jj)] <= nextDistance:
                    continue
                indexToMinDist[(ii, jj)] = nextDistance
                heappush(pq, [nextDistance, ii, jj])

        return -1
