class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] means whether s[i:j + 1] is palindrome
        dp = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # j is the length of the substring
        for j in range(3, n + 1):
            # i is the starting index of the substring
            for i in range(n - j + 1):
                if dp[i + 1][i + j - 2] and s[i] == s[i + j - 1]:
                    dp[i][i + j - 1] = True

        numOfSubstrs = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j]:
                    numOfSubstrs += 1
        return numOfSubstrs
