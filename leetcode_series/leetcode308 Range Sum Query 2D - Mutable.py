# O(lgm * lgn) Binary Index Tree solution for update and sumRegion.

from copy import deepcopy
class NumMatrix(object):

    def __init__(self, matrix):

        self.matrix = deepcopy(matrix)
        self.m, self.n = len(matrix), len(matrix[0]) if matrix else 0
        # medium is just a intermediate matrix for building the bit
        medium = [[0 for j in xrange(self.n + 1)] for i in xrange(self.m + 1)]
        self.bit = [[0 for j in xrange(self.n + 1)] for i in xrange(self.m + 1)]
        for i in xrange(1, self.m + 1):
            for j in xrange(self.n):
                k = j + 1
                while k < self.n + 1:
                    medium[i][k] += matrix[i - 1][j]
                    k += k & (-k)
        for j in xrange(1, self.n + 1):
            for i in xrange(1, self.m + 1):
                k = i
                while k < self.m + 1:
                    self.bit[k][j] += medium[i][j]
                    k += k & (-k)

    def update(self, row, col, val):

        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i < len(self.bit):
            k = col + 1
            while k < self.n + 1:
                self.bit[i][k] += diff
                k += k & (-k)
            i += i & (-i)

    def sumRegion(self, row1, col1, row2, col2):

        def sumrowcol(row, col):
            s = 0
            i = row
            while i > 0:
                j = col
                while j > 0:
                    s += self.bit[i][j]
                    j -= j & (-j)
                i -= i & (-i)
            return s

        ans = sumrowcol(row2 + 1, col2 + 1) + sumrowcol(row1, col1) - \
            sumrowcol(row1, col2 + 1) - sumrowcol(row2 + 1, col1)

        return ans



matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
Sol = NumMatrix(matrix)
Sol.update(1,0,1)
print Sol.sumRegion(2,1,4,3)
Sol.update(3,2,2)
print Sol.sumRegion(2,1,4,3)

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)



'''
# O(n) solution for sum abd update function. Keep a accumulate sum matrix of each row

from copy import deepcopy
class NumMatrix(object):

    def __init__(self, matrix):

        self.matrix = deepcopy(matrix)
        self.sumarray = deepcopy(matrix)
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if j > 0:
                    self.sumarray[i][j] += self.sumarray[i][j - 1]


    def update(self, row, col, val):

        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for j in xrange(col, len(self.sumarray[0])):
            self.sumarray[row][j] += diff


    def sumRegion(self, row1, col1, row2, col2):

        ans = 0
        for i in xrange(row1, row2 + 1):
            if col1 > 0:
                ans += self.sumarray[i][col2] - self.sumarray[i][col1 - 1]
            else:
                ans += self.sumarray[i][col2]

        return ans
'''
