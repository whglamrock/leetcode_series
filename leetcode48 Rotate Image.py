
# the idea is to go from the outer layer to the more insider ones.
class Solution(object):
    def rotate(self, matrix):

        n = len(matrix)
        # we go from outer layer to inner layer; i means the layer number
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp


matrix = [
  [5, 1, 9, 11],
  [2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
]
Solution().rotate(matrix)
for item in matrix:
    print(item)
