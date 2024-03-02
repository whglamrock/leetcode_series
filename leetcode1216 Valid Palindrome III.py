class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        lenOfLongestPalindromeSubsqns = self.longestPalindromeSubsequence(s)
        return len(s) - lenOfLongestPalindromeSubsqns <= k

    def longestPalindromeSubsequence(self, s: str) -> int:
        n = len(s)
        # dp[i][j] means the length longest palindrome subsequence within s[i:j + 1]
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i > 1:
                dp[i - 1][i] = 2 if s[i] == s[i - 1] else 1

        # j is the length of the palindrome
        for j in range(2, n + 1):
            # i is the starting index
            for i in range(n - j + 1):
                dp[i][i + j - 1] = max(dp[i + 1][i + j - 1], dp[i][i + j - 2])
                if s[i] == s[i + j - 1]:
                    dp[i][i + j - 1] = max(dp[i][i + j - 1], dp[i + 1][i + j - 2] + 2)

        return dp[0][-1]


print(Solution().isValidPalindrome(s="abcdeca", k=2))
print(Solution().isValidPalindrome(s="abbababa", k=1))
