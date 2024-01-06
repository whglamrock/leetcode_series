from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        gridSum = self.sumOfGrid(grid)
        if gridSum == n * n:
            return Node(1, 1)
        elif gridSum == 0:
            return Node(0, 1)
        # need to divide the grid
        else:
            root = Node(1, 0)
            topLeft = self.construct(self.generateSubGrid(grid, 0, n // 2 - 1, 0, n // 2 - 1))
            topRight = self.construct(self.generateSubGrid(grid, 0, n // 2 - 1, n // 2, n - 1))
            bottomLeft = self.construct(self.generateSubGrid(grid, n // 2, n - 1, 0, n // 2 - 1))
            bottomRight = self.construct(self.generateSubGrid(grid, n // 2, n - 1, n // 2, n - 1))
            root.topLeft = topLeft
            root.topRight = topRight
            root.bottomLeft = bottomLeft
            root.bottomRight = bottomRight
            return root

    def generateSubGrid(self, grid: List[List[int]], x1: int, x2: int, y1: int, y2: int):
        newGrid = []
        for i in range(x1, x2 + 1):
            row = []
            for j in range(y1, y2 + 1):
                row.append(grid[i][j])
            newGrid.append(row)
        return newGrid

    def sumOfGrid(self, grid: List[List[int]]) -> int:
        totalSum = 0
        for row in grid:
            totalSum += sum(row)
        return totalSum



