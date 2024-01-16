class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] means if s[:i] matches with p[:j]
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1, 2):
            if p[j - 1] == '*':
                dp[0][j] |= dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # * matches nothing
                    dp[i][j] |= dp[i][j - 1]
                    # * offsets the previous char, p[i - 2]
                    if j >= 2:
                        dp[i][j] |= dp[i][j - 2]
                    # extend p by one more char to match
                    if j >= 2 and (p[j - 2] == '.' or p[j - 2] == s[i - 1]):
                        dp[i][j] |= dp[i - 1][j]

        return dp[-1][-1]


print(Solution().isMatch('bbbbb', 'b*'))
print(Solution().isMatch('bbbcbb', 'b*'))
print(Solution().isMatch('mississippi', 'mis*is*p*.'))
print(Solution().isMatch('av', '.*'))
