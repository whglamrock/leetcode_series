from typing import List, Dict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        indexToIsland = {}
        islandId = 0
        islandToArea = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.sinkTheIsland(grid, i, j, indexToIsland, islandId)
                    islandToArea[islandId] = area
                    islandId += 1

        # even if it's all 0 we can flip one 0 to 1.
        maxConnectedIsland = max(islandToArea.values()) if islandToArea else 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in indexToIsland:
                    continue
                neighborIslands = set()
                if i - 1 >= 0 and (i - 1, j) in indexToIsland:
                    neighborIslands.add(indexToIsland[(i - 1, j)])
                if i + 1 < len(grid) and (i + 1, j) in indexToIsland:
                    neighborIslands.add(indexToIsland[(i + 1, j)])
                if j - 1 >= 0 and (i, j - 1) in indexToIsland:
                    neighborIslands.add(indexToIsland[(i, j - 1)])
                if j + 1 < len(grid[0]) and (i, j + 1) in indexToIsland:
                    neighborIslands.add(indexToIsland[(i, j + 1)])

                connectedArea = 0
                for neighborIsland in neighborIslands:
                    connectedArea += islandToArea[neighborIsland]
                if connectedArea:
                    maxConnectedIsland = max(maxConnectedIsland, connectedArea + 1)

        return maxConnectedIsland

    def sinkTheIsland(self, grid: List[List[int]], i: int, j: int, indexToIsland: Dict[tuple, int], islandId: int):
        grid[i][j] = 0
        indexToIsland[(i, j)] = islandId
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        area = 1
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 1:
                area += self.sinkTheIsland(grid, ii, jj, indexToIsland, islandId)

        return area


grid1 = [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 0]]
print(Solution().largestIsland(grid1))
grid2 = [[1, 0, 0],
         [0, 1, 1],
         [0, 1, 1]]
print(Solution().largestIsland(grid2))
grid3 = [[1, 1],
         [1, 1]]
print(Solution().largestIsland(grid3))

