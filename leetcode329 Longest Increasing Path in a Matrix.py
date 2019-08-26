
# worst case O(V^2) solution, where V is number of vertex (V = m * n); but in reality it's better than V^2

class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = set()

        for i in xrange(m):
            for j in xrange(n):
                if self.isLocalMinimum(matrix, i, j):
                    memo.add((i, j))

        ans = 0
        while memo:
            ans += 1
            nextMemo = set()
            for i, j in memo:
                nextIncreasing = self.findNextIncreasingPoints(matrix, i, j)
                nextMemo |= nextIncreasing
            memo = nextMemo

        return ans

    def isLocalMinimum(self, matrix, i, j):
        if i - 1 >= 0 and matrix[i - 1][j] < matrix[i][j]:
            return False
        if i + 1 < len(matrix) and matrix[i + 1][j] < matrix[i][j]:
            return False
        if j - 1 >= 0 and matrix[i][j - 1] < matrix[i][j]:
            return False
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] < matrix[i][j]:
            return False
        return True

    def findNextIncreasingPoints(self, matrix, i, j):
        nextIncreasing = set()
        if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
            nextIncreasing.add((i - 1, j))
        if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
            nextIncreasing.add((i + 1, j))
        if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
            nextIncreasing.add((i, j - 1))
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
            nextIncreasing.add((i, j + 1))

        return nextIncreasing



print Solution().longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
])
print Solution().longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
])
print Solution().longestIncreasingPath([
  [2,2,2],
  [2,2,2],
  [2,2,2]
])
print Solution().longestIncreasingPath([
  [2,2,2],
  [2,2,2],
  [2,0,1]
])



'''
class Solution(object):
    def longestIncreasingPath(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in xrange(n)] for i in xrange(m)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if (i > 0 and matrix[i - 1][j] > val) else 0,
                    dfs(i + 1, j) if (i < m - 1 and matrix[i + 1][j] > val) else 0,
                    dfs(i, j - 1) if (j > 0 and matrix[i][j - 1] > val) else 0,
                    dfs(i, j + 1) if (j < n - 1 and matrix[i][j + 1] > val) else 0)
            return dp[i][j]

        return max(dfs(x, y) for x in xrange(m) for y in xrange(n))
'''
