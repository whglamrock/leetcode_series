
# Overlapping is allowed. The description isn't clear enough.
# The O(N ^ 2) dp solution is the most practical optimal solution you can come up in real interview
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        # dp[i][j] == length means a match between s[i - length + 1:i + 1], s[j - length + 1:j + 1]
        dp = [[0 for j in range(n)] for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i - 1 >= 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                    ans = max(ans, dp[i][j])

        return ans
