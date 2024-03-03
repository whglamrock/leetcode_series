from collections import defaultdict
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.topLeftCornerSum = defaultdict(int)
        for i, row in enumerate(matrix):
            prefixSum = 0
            for j, num in enumerate(row):
                prefixSum += num
                if i == 0:
                    self.topLeftCornerSum[(0, j)] = prefixSum
                else:
                    self.topLeftCornerSum[(i, j)] = self.topLeftCornerSum[(i - 1, j)] + prefixSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # the defaultdict trick makes sure if any key not in the dict, it will return 0
        return self.topLeftCornerSum[(row2, col2)] \
            - self.topLeftCornerSum[(row1 - 1, col2)] \
            - self.topLeftCornerSum[(row2, col1 - 1)] \
            + self.topLeftCornerSum[(row1 - 1, col1 - 1)]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
