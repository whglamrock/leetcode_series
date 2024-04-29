
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # dp[1] means the min flips to make s[:i + 1] monotone increasing if s[i] is 0/1
        dp1, dp0 = [0] * n, [0] * n
        if s[0] == '0':
            dp1[0] = 1
        else:
            dp0[0] = 1

        for i in range(1, n):
            if s[i] == '0':
                dp0[i] = dp0[i - 1]
                dp1[i] = min(dp1[i - 1], dp0[i - 1]) + 1
            else:
                dp0[i] = dp0[i - 1] + 1
                dp1[i] = min(dp1[i - 1], dp0[i - 1])

        return min(dp0[-1], dp1[-1])
