from typing import List, Tuple

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            i, j = self.convertArrayIndexToMatrixIndex(m, len(matrix[0]))
            if l == r:
                return matrix[i][j] == target
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m + 1
            else:
                r = m

        return False

    def convertArrayIndexToMatrixIndex(self, arrayIndex: int, n: int) -> Tuple[int, int]:
        i = arrayIndex // n
        j = arrayIndex - i * n
        return i, j
