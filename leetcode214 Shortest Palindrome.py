# below O(N^2) solution definitely suffice any real interview requirement. The stupid motherfucking leetcode gives MLE
# If O(N^2) time & O(N) space solution is required we can simply brute force it (see short code solution at the bottom)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # j is the length of the palindrome
        for j in range(3, n + 1):
            # i is the starting index
            for i in range(n - j + 1):
                if s[i] == s[i + j - 1] and dp[i + 1][i + j - 2]:
                    dp[i][i + j - 1] = True

        for i in range(n - 1, -1, -1):
            if dp[0][i]:
                suffix = s[i + 1:]
                return suffix[::-1] + s


'''
# O(N) KMP algorithm solution
class Solution(object):
    def shortestPalindrome(self, s):

        # to calculate the 'pattern' of 'haystack'.
        def ComputePrefixFunction(needle):

            pat = [0] * len(needle)
            # j is the prefix pointer, i is the suffix pointer
            j, i = 0, 1
            while i < len(needle):
                if needle[i] == needle[j]:
                    pat[i] = j + 1
                    i += 1
                    j += 1
                elif j == 0:
                    pat[i] = 0
                    i += 1
                else:
                    j = pat[j - 1]

            return pat

        news = s + '#' + s[::-1]
        # the trick is to use KMP table to find the longest matching prefix of news
        KMPtable = ComputePrefixFunction(news)
        compensate = s[:KMPtable[-1] - 1:-1]

        return compensate + s
'''


'''
# quick O(N^2) time but O(N) space solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
            
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s
'''