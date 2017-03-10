# modify the matrix in-place instead of creating a new matrix
# the idea is to go from the outer layer to the more insider ones.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(n/2):
            for j in xrange(i,n-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp

        # return matrix   # in leetcode, delete this row cuz they do not fucking need any return values.

