# O(N^2) time, O(1) space solution.
class Solution(object):
    def maximalSquare(self, matrix):

        if (not matrix) or (not matrix[0]):
            return 0

        def check(i, j, i0, j0):
            for row in xrange(i0, i + 1):
                if matrix[row][j] == '0':
                    return False
            for col in xrange(j0, j + 1):
                if matrix[i][col] == '0':
                    return False
            return True

        ans = 0
        for i in xrange(len(matrix)):
            if len(matrix) - i <= ans: break
            for j in xrange(len(matrix[0])):
                if len(matrix[0]) - j <= ans: break
                edge = 0
                if matrix[i][j] == '1':
                    edge += 1
                    row, col = i + 1, j + 1
                    while row < len(matrix) and col < len(matrix[0]) and check(row, col, i, j):
                        row += 1
                        col += 1
                        edge += 1
                ans = max(ans, edge)

        return ans * ans

Sol = Solution()
matrix = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]
print Sol.maximalSquare(matrix)