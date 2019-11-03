
# O(M * N) DFS + memoization solution because each (i, j) will be only visited once.
    # This is the most practical to be given in real interview.

# P.S. Graph theory way can achieve O(V^2) (O(V^2) for building the graph and O(V) for DFS)
    # but is more complicated and error-prune.

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        ans = 0
        memo = {}
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                longest = self.dfs(matrix, i, j, memo)
                ans = max(ans, longest)

        return ans

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        up, down, left, right = 0, 0, 0, 0
        num = matrix[i][j]

        if i - 1 >= 0 and matrix[i - 1][j] > num:
            up = self.dfs(matrix, i - 1, j, memo)
        if i + 1 < len(matrix) and matrix[i + 1][j] > num:
            down = self.dfs(matrix, i + 1, j, memo)
        if j - 1 >= 0 and matrix[i][j - 1] > num:
            left = self.dfs(matrix, i, j - 1, memo)
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] > num:
            right = self.dfs(matrix, i, j + 1, memo)

        res = 1 + max(up, down, left, right)
        memo[(i, j)] = res
        return res



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