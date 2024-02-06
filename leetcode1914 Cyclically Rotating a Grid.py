from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        numOfLayers = min(len(grid), len(grid[0])) // 2
        for layerIndex in range(numOfLayers):
            layer = self.generateLayer(grid, layerIndex)
            self.rotateLayer(layer, k, grid)

        return grid

    def rotateLayer(self, layer: List[List[int]], k: int, grid: List[List[int]]):
        for index in range(len(layer)):
            i, j, val = layer[index]
            ii, jj, nextVal = layer[(index + k) % len(layer)]
            grid[ii][jj] = val

    def generateLayer(self, grid: List[List[int]], layerIndex: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layer = []

        # top edge
        for j in range(n - layerIndex - 1, layerIndex - 1, -1):
            layer.append([layerIndex, j, grid[layerIndex][j]])
        layer.pop()

        # left edge
        for i in range(layerIndex, m - layerIndex):
            layer.append([i, layerIndex, grid[i][layerIndex]])
        layer.pop()

        # bottom edge
        for j in range(layerIndex, n - layerIndex):
            layer.append([m - layerIndex - 1, j, grid[m - layerIndex - 1][j]])
        layer.pop()

        # right edge
        for i in range(m - layerIndex - 1, layerIndex - 1, -1):
            layer.append([i, n - 1 - layerIndex, grid[i][n - 1 - layerIndex]])
        layer.pop()

        return layer


print(Solution().rotateGrid(
    grid=[[40, 10],
          [30, 20]],
    k=1))
print(Solution().rotateGrid(
    grid=[[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]],
    k=2))
