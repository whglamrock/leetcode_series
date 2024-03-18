class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        maxLength = 0
        for i in range(m):
            for j in range(n):
                maxLength = max(maxLength, dp[i][j])

        return maxLength * maxLength


matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']]
print(Solution().maximalSquare(matrix))
