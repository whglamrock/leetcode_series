from copy import deepcopy


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        indexToArea = {}
        n = len(grid)
        # copy the grid to do dfs ("sink the island" idea in the classic Number of Islands problem)
        grid_copy = deepcopy(grid)
        connectedIndexes = {}

        # the islandId records which island each index belongs to
        islandId = 0
        ans = 0
        for i in range(n):
            for j in range(n):
                sunkIndexes = set()
                # all connected 1's will become 0 so islandId will always be accurate
                if grid_copy[i][j] == 1:
                    self.dfs(i, j, grid_copy, sunkIndexes)
                    for index in sunkIndexes:
                        indexToArea[index] = len(sunkIndexes)
                        connectedIndexes[index] = islandId
                    islandId += 1
                    ans = max(ans, len(sunkIndexes))

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                areaConnected = 0
                # usedIslands is to dedupe the island ID being used
                usedIslands = set()
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    areaConnected += indexToArea[(i - 1, j)]
                    usedIslands.add(connectedIndexes[(i - 1, j)])
                if i + 1 < n and grid[i + 1][j] == 1:
                    if connectedIndexes[(i + 1, j)] not in usedIslands:
                        areaConnected += indexToArea[(i + 1, j)]
                        usedIslands.add(connectedIndexes[(i + 1, j)])
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    if connectedIndexes[(i, j - 1)] not in usedIslands:
                        areaConnected += indexToArea[(i, j - 1)]
                        usedIslands.add(connectedIndexes[(i, j - 1)])
                if j + 1 < n and grid[i][j + 1] == 1:
                    if connectedIndexes[(i, j + 1)] not in usedIslands:
                        areaConnected += indexToArea[(i, j + 1)]
                        usedIslands.add(connectedIndexes[(i, j + 1)])
                ans = max(ans, areaConnected + 1)

        return ans

    # sink the island and record the indexes
    def dfs(self, i, j, grid, sunkIndexes):
        if grid[i][j] == 0:
            return
        if grid[i][j] == 1:
            grid[i][j] = 0
            sunkIndexes.add((i, j))
        if i - 1 >= 0:
            self.dfs(i - 1, j, grid, sunkIndexes)
        if i + 1 < len(grid):
            self.dfs(i + 1, j, grid, sunkIndexes)
        if j - 1 >= 0:
            self.dfs(i, j - 1, grid, sunkIndexes)
        if j + 1 < len(grid[0]):
            self.dfs(i, j + 1, grid, sunkIndexes)


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

