
# I don't know why the fuck the stupid leetcode only accepts this O(M + N) solution and gives MLE for
# the O(M * N) dp solution. The dp solution is definitely acceptable in real interview.
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        i, j = 0, 0
        while i < m and j < n:
            if str1[i] == str2[j] or ord(str2[j]) - ord(str1[i]) == 1 or ord(str1[i]) - ord(str2[j]) == 25:
                i += 1
                j += 1
            else:
                i += 1

        return j == n


print(Solution().canMakeSubsequence(str1="abc", str2="ad"))
print(Solution().canMakeSubsequence(str1="zc", str2="ad"))


'''
# below O(M * N) dp solution is definitely acceptable in real interview.
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        
        m, n = len(str1), len(str2)
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = True

        for i in range(1, m +1):
            for j in range(1, n + 1):
                # see if str1[:i - 1] can turn into super sequence of str2
                dp[i][j] = dp[i - 1][j]
                if str1[i - 1] == str2[j - 1] or ord(str2[j - 1]) - ord(str1[i - 1]) == 1 or (str1[i - 1] == 'z' and str2[j - 1] == 'a'):
                    dp[i][j] |= dp[i - 1][j - 1]
        
        return dp[-1][-1]
'''