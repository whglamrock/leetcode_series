from collections import defaultdict
from typing import List, Dict

# when calculating the string shape of an island, we don't need to sort the indexes for each row because the order &
# starting point of doing dfs is unchanged if it's the same shape. This means: for certain island shape,
# within each row, the indexes of 1's are added to the value list of map in the same order.
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islandShapes = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowTo1Indexes = defaultdict(list)
                    self.dfs(grid, i, j, rowTo1Indexes)
                    shape = []
                    for k in range(min(rowTo1Indexes.keys()), max(rowTo1Indexes.keys()) + 1):
                        valueList = rowTo1Indexes[k]
                        rowShape = ','.join(str(value - j) for value in valueList)
                        shape.append(rowShape)
                    islandShapes.add('_'.join(shape))

        return len(islandShapes)

    def dfs(self, grid: List[List[int]], i: int, j: int, rowTo1Indexes: Dict[int, List[int]]):
        grid[i][j] = 0
        rowTo1Indexes[i].append(j)

        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                self.dfs(grid, ii, jj, rowTo1Indexes)
