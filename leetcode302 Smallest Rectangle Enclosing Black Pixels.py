from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # find the first row
        firstRow = x
        top, bottom = 0, x
        while top <= bottom:
            m = (top + bottom) // 2
            if top == bottom:
                firstRow = m
                break
            if '1' in image[m]:
                bottom = m
            else:
                top = m + 1
        # find the last row
        lastRow = x
        top, bottom = x, len(image) - 1
        while top <= bottom:
            m = (top + bottom + 1) // 2
            if top == bottom:
                lastRow = m
                break
            if '1' in image[m]:
                top = m
            else:
                bottom = m - 1

        # find the first column
        firstCol = y
        left, right = 0, y
        while left <= right:
            m = (left + right) // 2
            if left == right:
                firstCol = m
                break
            is1InColumn = False
            for i in range(len(image)):
                if image[i][m] == '1':
                    is1InColumn = True
                    break
            if is1InColumn:
                right = m
            else:
                left = m + 1
        # find the last column
        lastCol = y
        left, right = y, len(image[0]) - 1
        while left <= right:
            m = (left + right + 1) // 2
            if left == right:
                lastCol = m
                break
            is1InColumn = False
            for i in range(len(image)):
                if image[i][m] == '1':
                    is1InColumn = True
                    break
            if is1InColumn:
                left = m
            else:
                right = m - 1

        return (lastRow - firstRow + 1) * (lastCol - firstCol + 1)


'''
# simple dfs solution
class Solution:
    def __init__(self):
        self.maxY = 0
        self.minY = 0
        self.maxX = 0
        self.minX = 0

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.minX, self.maxX = 2147483647, -2147483648
        self.minY, self.maxY = 2147483647, -2147483648
        self.dfs(image, x, y)
        # print(self.minX, self.maxX, self.minY, self.maxY)
        return (self.maxX - self.minX + 1) * (self.maxY - self.minY + 1)

    def dfs(self, image: List[List[str]], i: int, j: int):
        image[i][j] = '0'
        self.minX = min(self.minX, i)
        self.maxX = max(self.maxX, i)
        self.minY = min(self.minY, j)
        self.maxY = max(self.maxY, j)

        m, n = len(image), len(image[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if 0 <= ii < m and 0 <= jj < n and image[ii][jj] == '1':
                self.dfs(image, ii, jj)
'''
