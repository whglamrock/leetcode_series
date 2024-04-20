class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] means the edit distance between word1[:i] and word2[:j]
        dp = [[2147483647 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # insert a char or delete a char
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                # replace a char
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[-1][-1]


print(Solution().minDistance('afsag', 'rthates'))
