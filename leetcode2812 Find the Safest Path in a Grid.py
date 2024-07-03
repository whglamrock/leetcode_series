from heapq import *
from typing import List


# BFS + Dijkstra. O(N^2 * log(N^2)) time complexity
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        todo = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    todo.append((i, j))

        # do bfs to get cell to safeness map
        cellToSafeness = {}
        distFromThief = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while todo:
            nextTodo = set()
            for (i, j) in todo:
                if (i, j) in cellToSafeness:
                    continue
                cellToSafeness[(i, j)] = distFromThief
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < n and 0 <= jj < n and (ii, jj) not in cellToSafeness:
                        nextTodo.add((ii, jj))
            todo = nextTodo
            distFromThief += 1

        cellToCurrHighestSafeness = {}
        # pq saves the highest safeness seen so far in all the paths that pass through (i, j)
        pq = []
        heappush(pq, [-cellToSafeness[(0, 0)], 0, 0])
        while pq:
            safeness, i, j = heappop(pq)
            safeness = -safeness

            if i == n - 1 and j == n - 1:
                return safeness

            if (i, j) not in cellToCurrHighestSafeness or cellToCurrHighestSafeness[(i, j)] < safeness:
                cellToCurrHighestSafeness[(i, j)] = safeness

            for deltaI, deltaJ in directions:
                ii, jj = i + deltaI, j + deltaJ
                if ii < 0 or ii >= n or jj < 0 or jj >= n:
                    continue

                # do no get into the next cell if we can' achieve a higher safeness score
                newSafeness = min(cellToSafeness[(ii, jj)], safeness)
                if (ii, jj) not in cellToCurrHighestSafeness or cellToCurrHighestSafeness[(ii, jj)] < newSafeness:
                    heappush(pq, [-newSafeness, ii, jj])
                    cellToCurrHighestSafeness[(ii, jj)] = newSafeness

        return -1


print(Solution().maximumSafenessFactor(grid=[
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]]))
print(Solution().maximumSafenessFactor(grid=[
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]]))
print(Solution().maximumSafenessFactor(grid=[
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0]]))
