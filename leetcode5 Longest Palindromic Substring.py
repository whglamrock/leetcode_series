# For Manacher algorithm O(N) solution, see: https://leetcode.com/problems/longest-palindromic-substring/discuss/3337
# /Manacher-algorithm-in-Python-O(n) In real interview, we only need to mention the Manacher algorithm. It will
# be really stupid if a company actually requires O(N) solution Following is O(N^2) solution. P.S.: notice the
# direction of j, i indices' iterations in dp!

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]

        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # i is the left index, j is right index
        # at this point, any new palindromes will be at least 3 chars long
        for j in range(2, n):
            for i in range(j - 2, -1, -1):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True

        maxLen = 0
        l, r = 0, 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    l, r = i, j

        return s[l:r + 1]


print(Solution().longestPalindrome("abcba"))
print(Solution().longestPalindrome("abccba"))
print(Solution().longestPalindrome("abceba"))
