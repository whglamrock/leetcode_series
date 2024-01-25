from typing import List, Dict

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        distances = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    buildings.append([i, j])
                    indexToDistance = {}
                    self.bfs(grid, i, j, indexToDistance)
                    distances.append(indexToDistance)

        minDistance = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    continue
                isBuildable = True
                distanceSum = 0
                for indexToDistance in distances:
                    if (i, j) not in indexToDistance:
                        isBuildable = False
                        break
                    distanceSum += indexToDistance[(i, j)]
                if isBuildable:
                    minDistance = min(minDistance, distanceSum)

        return minDistance if minDistance != 2147483647 else -1

    def bfs(self, grid: List[List[int]], x: int, y: int, indexToDistance: Dict[tuple, int]):
        todo = {(x, y)}
        currDistance = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while todo:
            nextTodo = set()
            for i, j in todo:
                indexToDistance[(i, j)] = currDistance
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 0 and (ii, jj) not in indexToDistance:
                        nextTodo.add((ii, jj))
            todo = nextTodo
            currDistance += 1
