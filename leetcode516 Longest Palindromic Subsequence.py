
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        # j is the length
        for j in range(1, n + 1):
            # i is the starting index
            for i in range(n - j + 1):
                if j == 1:
                    dp[i][i + j - 1] = 1
                    continue
                if j == 2 and i + 1 < n and s[i] == s[i + 1]:
                    dp[i][i + 1] = 2
                    continue
                if s[i] == s[i + j - 1]:
                    dp[i][i + j - 1] = dp[i + 1][i + j - 2] + 2
                else:
                    dp[i][i + j - 1] = max(dp[i][i + j - 2], dp[i + 1][i + j - 1])

        return dp[0][-1]


Sol = Solution()
s = 'abasfba'
print(Sol.longestPalindromeSubseq(s))
