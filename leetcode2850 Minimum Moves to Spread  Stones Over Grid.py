from copy import deepcopy
from typing import List

# Find min move uses dfs approach, should be acceptable in real interview.
# We can try to use lru_cache to speed up the dfs by serialize the stonesToMove and emptyCell parameters
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        stonesToMove = []
        emptyCells = set()
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 1:
                    continue
                if grid[i][j] == 0:
                    emptyCells.add((i, j))
                    continue
                for k in range(grid[i][j] - 1):
                    stonesToMove.append([i, j])

        return self.findMinMoves(stonesToMove, emptyCells)

    def findMinMoves(self, stonesToMove: List[List[int]], emptyCells: set) -> int:
        if not stonesToMove:
            return 0

        minMoves = 2147483647
        for i, j in emptyCells:
            dist = abs(i - stonesToMove[0][0]) + abs(j - stonesToMove[0][1])
            newEmptyCells = deepcopy(emptyCells)
            newEmptyCells.discard((i, j))
            minMoves = min(minMoves, dist + self.findMinMoves(stonesToMove[1:], newEmptyCells))

        return minMoves
