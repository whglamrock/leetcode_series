
class Solution(object):
    def imageSmoother(self, M):

        if not M or not M[0]:
            return M

        m, n = len(M), len(M[0])
        res = [[0 for y in xrange(n)] for x in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                sumOfSurroundings = M[i][j]
                count = 1  # starting from counting (i, j) itself
                if i - 1 >= 0 and j - 1 >= 0:
                    sumOfSurroundings += M[i - 1][j - 1]
                    count += 1
                if i - 1 >= 0:
                    sumOfSurroundings += M[i - 1][j]
                    count += 1
                if i - 1 >= 0 and 0 <= j + 1 < n:
                    sumOfSurroundings += M[i - 1][j + 1]
                    count += 1
                if j - 1 >= 0:
                    sumOfSurroundings += M[i][j - 1]
                    count += 1
                if j + 1 < n:
                    sumOfSurroundings += M[i][j + 1]
                    count += 1
                if i + 1 < m and j - 1 >= 0:
                    sumOfSurroundings += M[i + 1][j - 1]
                    count += 1
                if i + 1 < m:
                    sumOfSurroundings += M[i + 1][j]
                    count += 1
                if i + 1 < m and j + 1 < n:
                    sumOfSurroundings += M[i + 1][j + 1]
                    count += 1
                res[i][j] = int(sumOfSurroundings / count)

        return res


