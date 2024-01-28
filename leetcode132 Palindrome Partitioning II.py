class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # j is the length of the palindrome
        for j in range(3, n + 1):
            for i in range(n - j + 1):
                if s[i] == s[i + j - 1] and dp[i + 1][i + j - 2]:
                    dp[i][i + j - 1] = True

        # cut[i] stores the min cut for s[:i + 1]
        cut = [i for i in range(n)]
        for i in range(1, n):
            if dp[0][i]:
                cut[i] = 0
                continue
            for j in range(i):
                if dp[j + 1][i]:
                    cut[i] = min(cut[i], cut[j] + 1)
        return cut[-1]


print(Solution().minCut('aacaddqw'))
print(Solution().minCut('aaaabbaaaabaa'))


'''
# dp array + cached dfs solution that should also be acceptable in real interview
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        self.dp = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            self.dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                self.dp[i][i + 1] = True
        
        # j is the length of the palindrome
        for j in range(3, n + 1):
            for i in range(n - j + 1):
                if s[i] == s[i + j - 1] and self.dp[i + 1][i + j - 2]:
                    self.dp[i][i + j - 1] = True
        
        return self.dfs(s, 0)
        
    @lru_cache(None)
    def dfs(self, s: str, i: int) -> int:
        if not s or self.dp[i][-1]:
            return 0

        minCut = len(s) - i - 1
        # cut the s so it becomes s[i:j + 1] and s[j + 1:]
        for j in range(i, len(s) - 1):
            if self.dp[i][j]:
                numOfCuts = 1 + self.dfs(s, j + 1)
                minCut = min(minCut, numOfCuts)
        
        return minCut
'''
