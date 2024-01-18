class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        m, n = len(s), len(p)
        # dp[i][j] means whether s[:i] matches with p[:j]
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True
        # deal with the case where the prefix of p is all "*"s
        for j in range(1, n + 1):
            if p[j - 1] != '*':
                break
            for i in range(m + 1):
                dp[i][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # * matches one more char
                    dp[i][j] |= dp[i - 1][j]
                    # * matches 0 char
                    dp[i][j] |= dp[i][j - 1]
                    # dp[i][j] |= dp[i - 1][j - 1] is not necessary because if dp[i - 1][j - 1] is true
                    # dp[i - 1][j] is 100% true (* matches 0 char)

        return dp[-1][-1]


print(Solution().isMatch('adceb', '*a*b'))
print(Solution().isMatch('acdcb', 'a*c?b'))
print(Solution().isMatch("ho", "**ho"))
print(Solution().isMatch("a", ""))
print(Solution().isMatch("aa", "*"))
print(Solution().isMatch("a", "aa"))
print(Solution().isMatch("", "******"))
