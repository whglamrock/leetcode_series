# idea is dp.
class NumMatrix(object):
    def __init__(self, matrix):

        if (not matrix) or (not matrix[0]):
            return
        self.summatrix = [[0 for j in xrange(len(matrix[0]) + 1)] for i in xrange(len(matrix) + 1)]
        self.summatrix[1][1] = matrix[0][0]
        for i in xrange(1, len(matrix)):
            self.summatrix[i + 1][1] = self.summatrix[i][1] + matrix[i][0]
        for j in xrange(1, len(matrix[0])):
            self.summatrix[1][j + 1] = self.summatrix[1][j] + matrix[0][j]
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                self.summatrix[i + 1][j + 1] = self.summatrix[i][j + 1] + self.summatrix[i + 1][j] - self.summatrix[i][j] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):

        return self.summatrix[row2 + 1][col2 + 1] + self.summatrix[row1][col1] - self.summatrix[row2 + 1][col1] - self.summatrix[row1][col2 + 1]


matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
Sol = NumMatrix(matrix)
print Sol.sumRegion(1, 1, 2, 2)




# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)