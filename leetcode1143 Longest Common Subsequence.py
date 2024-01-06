
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # dp[i][j] stores the length of the LCS between text1[:i] & text2[:j]
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))
print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))
print(Solution().longestCommonSubsequence(text1="abc", text2="def"))
