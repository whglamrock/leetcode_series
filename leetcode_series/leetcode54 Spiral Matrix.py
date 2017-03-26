
# very elegant solution by modifying the matrix. Since we pop elements from matrix,
# there won't be index out range issue.

class Solution(object):
    def spiralOrder(self, matrix):

        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret



Sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print Sol.spiralOrder(matrix)



'''
# my orignal ugly but somehow a bit efficient solution
class Solution(object):
    def spiralOrder(self, matrix):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        visited = [[0 for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
        countdown = len(matrix)*len(matrix[0])
        ans = []

        i, j = 0, 0
        direction = 'right'
        while countdown > 0:
            ans.append(matrix[i][j])
            visited[i][j] += 1
            countdown -= 1
            if direction == 'right':
                if j < len(matrix[0])-1:
                    j += 1
                if visited[i][j] != 0:
                    if j > 0:
                        j -= 1
                    direction = 'down'
                    if i < len(matrix)-1:
                        i += 1
                elif j == len(matrix[0])-1:
                    direction = 'down'
                continue
            if direction == 'down':
                if i < len(matrix)-1:
                    i += 1
                if visited[i][j] != 0:
                    if i > 0:
                        i -= 1
                    direction = 'left'
                    if j > 0:
                        j -= 1
                elif i == len(matrix)-1:
                    direction = 'left'
                continue
            if direction == 'left':
                if j > 0:
                    j -= 1
                if visited[i][j] != 0:
                    if j < len(matrix[0])-1:
                        j += 1
                    direction = 'up'
                    if i > 0:
                        i -= 1
                elif j == 0:
                    direction = 'up'
                continue
            if direction == 'up':
                if i > 0:
                    i -= 1
                if visited[i][j] != 0:
                    if i < len(matrix)-1:
                        i += 1
                    direction = 'right'
                    if j < len(matrix[0])-1:
                        j += 1
                elif i == 0:
                    direction = 'right'
                continue

        return ans
'''
