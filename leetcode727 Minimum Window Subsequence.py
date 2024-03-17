
# Since len(s1) >> len(s2) and len(s1) can be 2 * 10 ^ 4, any O(N ^ 2) solution won't work. We have to use DP.
# Below is O(m * n) DP solution. dp[i][j] means the min length of s1 substring that ends at s1[i - 1] and is a super sequence of s2[:j]
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[2147483647 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                # if s1[:i - 1] is already a super sequence of s2[:j]
                dp[i][j] = dp[i - 1][j] + 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

        minLen = min(dp[i][-1] for i in range(1, m + 1))
        if minLen >= 2147483647:
            return ''
        for i in range(1, m + 1):
            if dp[i][-1] == minLen:
                return s1[i - minLen:i]


print(Solution().minWindow(s1="abcdebdde", s2="bde"))
