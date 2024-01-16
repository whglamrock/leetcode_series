class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        if s[0] != '0':
            dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                if i >= 2:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1

        return dp[-1]
