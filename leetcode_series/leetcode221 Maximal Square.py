
# O(N^2) time, O(N^2) space DP solution; or we can maintain two 1 * n vector dp and pre-dp
#   to cut the space to O(N)
# Only the DP solution can guarantee O(N^2) time complexity

class Solution(object):
    def maximalSquare(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        ans = 0
        for i in xrange(m):
            themaxofthisline = max(dp[i][j] for j in xrange(n))
            ans = max(ans, themaxofthisline)

        return ans * ans



Sol = Solution()
matrix = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]
print Sol.maximalSquare(matrix)