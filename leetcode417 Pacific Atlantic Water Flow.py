
class Solution(object):
    def pacificAtlantic(self, matrix):

        if (not matrix) or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        pacific = [[0 for j in xrange(n)] for i in xrange(m)]
        atlantic = [[0 for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            if i == 0:
                for j in xrange(n):
                    pacific[0][j] = 1
                atlantic[0][-1] = 1
            if i == m - 1:
                for j in xrange(n):
                    atlantic[m - 1][j] = 1
                pacific[m - 1][0] = 1
            else:
                pacific[i][0] = 1
                atlantic[i][-1] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if pacific[i][j] == 1:
                    continue
                if pacific[i - 1][j] == 1 and matrix[i - 1][j] <= matrix[i][j]:
                    pacific[i][j] = 1
                elif pacific[i][j - 1] == 1 and matrix[i][j - 1] <= matrix[i][j]:
                    pacific[i][j] = 1
                elif i + 1 < m and pacific[i + 1][j] == 1 and matrix[i + 1][j] <= matrix[i][j]:
                    pacific[i][j] = 1
                elif j + 1 < n and pacific[i][j + 1] == 1 and matrix[i][j + 1] <= matrix[i][j]:
                    pacific[i][j] = 1
                if pacific[i][j] == 1:
                    todo = {(i, j)}
                    while todo:
                        next = set()
                        #if i == 1 and j == 1: print todo
                        for y, x in todo:
                            pacific[y][x] = 1
                            if y - 1 > 0 and pacific[y - 1][x] == 0 and matrix[y - 1][x] >= matrix[y][x]:
                                next.add((y - 1, x))
                            if x - 1 > 0 and pacific[y][x - 1] == 0 and matrix[y][x - 1] >= matrix[y][x]:
                                next.add((y, x - 1))
                            if y + 1 < m and pacific[y + 1][x] == 0 and matrix[y + 1][x] >= matrix[y][x]:
                                next.add((y + 1, x))
                            if x + 1 < n and pacific[y][x + 1] == 0 and matrix[y][x + 1] >= matrix[y][x]:
                                next.add((y, x + 1))
                        todo = next
                        #print pacific

        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                if atlantic[i][j] == 1:
                    continue
                if atlantic[i + 1][j] == 1 and matrix[i + 1][j] <= matrix[i][j]:
                    atlantic[i][j] = 1
                elif atlantic[i][j + 1] == 1 and matrix[i][j + 1] <= matrix[i][j]:
                    atlantic[i][j] = 1
                elif i - 1 > 0 and atlantic[i - 1][j] == 1 and matrix[i - 1][j] <= matrix[i][j]:
                    atlantic[i][j] = 1
                elif j - 1 > 0 and atlantic[i][j - 1] == 1 and matrix[i][j - 1] <= matrix[i][j]:
                    atlantic[i][j] = 1

                if atlantic[i][j] == 1:
                    todo = {(i, j)}
                    while todo:
                        next = set()
                        for y, x in todo:
                            atlantic[y][x] = 1
                            if y - 1 > 0 and atlantic[y - 1][x] == 0 and matrix[y - 1][x] >= matrix[y][x]:
                                next.add((y - 1, x))
                            if x - 1 > 0 and atlantic[y][x - 1] == 0 and matrix[y][x - 1] >= matrix[y][x]:
                                next.add((y, x - 1))
                            if y + 1 < m and atlantic[y + 1][x] == 0 and matrix[y + 1][x] >= matrix[y][x]:
                                next.add((y + 1, x))
                            if x + 1 < n and atlantic[y][x + 1] == 0 and matrix[y][x + 1] >= matrix[y][x]:
                                next.add((y, x + 1))
                        todo = next
        ans = []
        for i in xrange(m):
            for j in xrange(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append([i, j])

        return ans


