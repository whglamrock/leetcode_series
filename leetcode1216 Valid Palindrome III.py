
# At the bottom, there is a delete char dfs + cache solution, which can be a follow up from valid palindrome II
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        lenOfLongestPalindromeSubsqns = self.longestPalindromeSubsequence(s)
        return len(s) - lenOfLongestPalindromeSubsqns <= k

    def longestPalindromeSubsequence(self, s: str) -> int:
        n = len(s)
        # dp[i][j] means the length of the longest palindrome subsequence within s[i:j + 1]
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i > 1:
                dp[i - 1][i] = 2 if s[i] == s[i - 1] else 1

        # j is the length of the palindrome
        for j in range(3, n + 1):
            # i is the starting index
            for i in range(n - j + 1):
                dp[i][i + j - 1] = max(dp[i + 1][i + j - 1], dp[i][i + j - 2])
                if s[i] == s[i + j - 1]:
                    dp[i][i + j - 1] = max(dp[i][i + j - 1], dp[i + 1][i + j - 2] + 2)

        return dp[0][-1]


print(Solution().isValidPalindrome(s="abcdeca", k=2))
print(Solution().isValidPalindrome(s="abbababa", k=1))


'''
# delete char dfs + cache solution (AC in leetcode); it can get asked as follow-up in real interview
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return self.isValidKPalindrome(s, 0, len(s) - 1, k)
    
    @lru_cache(None)
    def isValidKPalindrome(self, s, l: int, r: int, k: int) -> bool:
        i, j = l, r
        while i < j:
            if s[i] != s[j]:
                if k <= 0:
                    return False
                return self.isValidKPalindrome(s, i + 1, j, k - 1) or self.isValidKPalindrome(s, i, j - 1, k - 1)
            i += 1
            j -= 1
        return True
'''