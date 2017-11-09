
# Two sweeps would be enough:
# no matter how far a "1" cell is from "0" cell, the shortest path will always
#   comes from the four neighbors. The first sweep that starts from the topleft
#   corner will guarantee this "1" cell finds the shortest path from left and top;
#   then the second sweep that starts from the bottom right corner will will
#   guarantee this "1" cell finds the shortest path from right and bottom.

class Solution(object):
    def updateMatrix(self, matrix):

        if not matrix or not matrix[0]:
            return matrix

        maxint = 2147483647
        m, n = len(matrix), len(matrix[0])
        res = [[maxint for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    continue
                if i > 0:
                    res[i][j] = min(res[i][j], 1 + res[i - 1][j])
                if j > 0:
                    res[i][j] = min(res[i][j], 1 + res[i][j - 1])

        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    continue
                if i < m - 1:
                    res[i][j] = min(res[i][j], 1 + res[i + 1][j])
                if j < n - 1:
                    res[i][j] = min(res[i][j], 1 + res[i][j + 1])

        return res



Sol = Solution()
matrix = [[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]]
print Sol.updateMatrix(matrix)
