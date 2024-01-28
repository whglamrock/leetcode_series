# The stupid leetcode doesn't accept dfs + memoization solution, only DP works in LC.
# But the cached dfs should work in real interview. See dfs approach at the bottom.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] means the number of subsequences of s[:i] to match t[:j]
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # not using s[i - 1], see if any subsequence generate t[:j]
                dp[i][j] = dp[i - 1][j]
                # use s[i - 1] to match t[j - 1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]


print(Solution().numDistinct("babagbag", "bag"))
print(Solution().numDistinct("rabbbit", "rabbit"))


'''
# dfs + cache/memoization solution
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.dfs(s, t, 0, 0)
    
    @lru_cache(None)
    def dfs(self, s: str, t: str, i: int, j: int) -> int:
        if j == len(t):
            return 1
        
        numOfWays = 0
        for ii in range(i, len(s)):
            if s[ii] == t[j]:
                numOfWays += self.dfs(s, t, ii + 1, j + 1)
        
        return numOfWays
'''