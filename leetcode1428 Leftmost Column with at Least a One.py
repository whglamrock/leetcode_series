from typing import List

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        pass

    def dimensions(self) -> List[int]:
        pass

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        numOfRows, numOfCols = dimensions[0], dimensions[1]
        r = numOfCols - 1
        for i in range(numOfRows):
            leftMostOne = self.findLeftMostOne(binaryMatrix, r, i)
            if leftMostOne == -1:
                continue
            r = min(r, leftMostOne)

        if r == numOfCols - 1 and binaryMatrix.get(numOfRows - 1, r) == 0:
            return -1

        return r

    def findLeftMostOne(self, binaryMatrix: 'BinaryMatrix', r: int, row: int) -> int:
        l = 0
        while l <= r:
            if l == r:
                if binaryMatrix.get(row, l) == 1:
                    return l
                else:
                    return -1
            m = (l + r) // 2
            if binaryMatrix.get(row, m) == 1:
                r = m
            else:
                l = m + 1

        return -1
