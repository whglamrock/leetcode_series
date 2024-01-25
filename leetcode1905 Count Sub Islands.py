from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands = []
        indexToIsland = {}
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1:
                    connectedIndexes = set()
                    self.sinkTheIsland(grid1, i, j, connectedIndexes)
                    islands.append(connectedIndexes)
                    for index in connectedIndexes:
                        indexToIsland[index] = len(islands) - 1

        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    connectedIndexes = set()
                    self.sinkTheIsland(grid2, i, j, connectedIndexes)
                    if (i, j) not in indexToIsland:
                        continue

                    islandIndexes1 = islands[indexToIsland[(i, j)]]
                    isSubIsland = True
                    for index in connectedIndexes:
                        if index not in islandIndexes1:
                            isSubIsland = False
                            break
                    if isSubIsland:
                        ans += 1

        return ans

    def sinkTheIsland(self, grid: List[List[int]], i: int, j: int, currIndexes: set):
        grid[i][j] = 0
        currIndexes.add((i, j))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 1:
                self.sinkTheIsland(grid, ii, jj, currIndexes)
