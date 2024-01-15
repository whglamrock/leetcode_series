# For Manacher algorithm O(N) solution, see: https://leetcode.com/problems/longest-palindromic-substring/discuss/3337
# /Manacher-algorithm-in-Python-O(n) In real interview, we only need to mention the Manacher algorithm. It will
# be really stupid if a company actually requires O(N) solution Following is O(N^2) solution. P.S.: notice the
# direction of j, i indices' iterations in dp!

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j] means if s[i:j + 1] is palindrome
        dp = [[False for j in range(n)] for i in range(n)]
        # prefill the dp array
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # j is the length
        for j in range(3, n + 1):
            # i is the starting index
            for i in range(n - j + 1):
                if s[i] == s[i + j - 1] and dp[i + 1][i + j - 2]:
                    dp[i][i + j - 1] = True

        maxLen = 1
        start, end = 0, 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j - i + 1 > maxLen:
                    start, end = i, j
                    maxLen = j - i + 1

        return s[start:end + 1]


print(Solution().longestPalindrome("abcba"))
print(Solution().longestPalindrome("abccba"))
print(Solution().longestPalindrome("abceba"))
