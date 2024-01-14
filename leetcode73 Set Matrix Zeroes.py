from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        firstColZero = False
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
        firstRowZero = False
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        # store the condition of each row and column in the first element of each row/column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # fill each row
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # fill rach column
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
