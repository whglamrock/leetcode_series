from collections import Counter
from typing import List


# A really stupid question which basically asks you to enumerate all scenarios
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        yCells, nonYCells = [], []
        for i in range(n):
            for j in range(n):
                # top left diagonal
                if i == j and i < n // 2:
                    yCells.append(grid[i][j])
                # top right diagonal
                elif i + j == n - 1 and i < n // 2:
                    yCells.append(grid[i][j])
                # center
                elif i == j and i == n // 2:
                    yCells.append(grid[i][j])
                # bottom half center line
                elif i > n // 2 and j == n // 2:
                    yCells.append(grid[i][j])
                else:
                    nonYCells.append(grid[i][j])

        yCellCounter = Counter(yCells)
        nonYCellCounter = Counter(nonYCells)

        # yCell == 0, nonYCell == 1
        numOfOperationsFor0YCell = yCellCounter[1] + yCellCounter[2]
        numOfOperationsFor1NonYCell = nonYCellCounter[0] + nonYCellCounter[2]
        minOperationCase1 = numOfOperationsFor0YCell + numOfOperationsFor1NonYCell

        # yCell == 0, nonYCell == 2
        numOfOperationsFor2NonYCell = nonYCellCounter[0] + nonYCellCounter[1]
        minOperationCase2 = numOfOperationsFor0YCell + numOfOperationsFor2NonYCell

        # yCell == 1, nonYCell == 0
        numOfOperationsFor1YCell = yCellCounter[0] + yCellCounter[2]
        numOfOperationsFor0NonYCell = nonYCellCounter[1] + nonYCellCounter[2]
        minOperationCase3 = numOfOperationsFor1YCell + numOfOperationsFor0NonYCell

        # yCell == 1, nonYCell == 2
        minOperationCase4 = numOfOperationsFor1YCell + numOfOperationsFor2NonYCell

        # yCell == 2, nonYCell == 0
        numOfOperationsFor2YCell = yCellCounter[0] + yCellCounter[1]
        minOperationCase5 = numOfOperationsFor2YCell + numOfOperationsFor0NonYCell

        # yCell == 2, nonYCell == 1
        minOperationCase6 = numOfOperationsFor2YCell + numOfOperationsFor1NonYCell

        return min(minOperationCase1, minOperationCase2, minOperationCase3, minOperationCase4, minOperationCase5, minOperationCase6)
