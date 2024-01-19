from typing import List

# Binary Index Tree solution will be more impressive in real interview
# see how BIT is constructed in a clean way: https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
# update: O(logN); sumRegion: O(M * logN)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.bits = []
        for i in range(m):
            bit = [0] * (n + 1)
            for j in range(1, n + 1):
                diff = matrix[i][j - 1]
                self.updateBIT(bit, diff, j)
            self.bits.append(bit)

    def update(self, row: int, col: int, val: int) -> None:
        self.updateBIT(self.bits[row], val - self.matrix[row][col], col + 1)
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.queryBIT(self.bits[i], col2 + 1) - self.queryBIT(self.bits[i], col1)
        return ans

    def updateBIT(self, bit: List[int], diff: int, i: int):
        while i < len(bit):
            bit[i] += diff
            i += (i & -i)

    def queryBIT(self, bit: List[int], i: int):
        ans = 0
        while i > 0:
            ans += bit[i]
            i -= (i & -i)
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
