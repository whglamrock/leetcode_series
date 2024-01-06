from typing import List

# idea is obviously finding the longest common subsequence. See leetcode1143
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        longestCommonSubsequence = self.longestCommonSubsequence(str1, str2)
        splitStrs1 = self.splitStringBySubsequence(longestCommonSubsequence, str1)
        splitStrs2 = self.splitStringBySubsequence(longestCommonSubsequence, str2)

        ans = []
        i, j = 0, 0
        while i < len(splitStrs1) and j < len(splitStrs2):
            while i < len(splitStrs1) and not splitStrs1[i].startswith("subsqs:"):
                ans.append(splitStrs1[i])
                i += 1
            while j < len(splitStrs2) and not splitStrs2[j].startswith("subsqs:"):
                ans.append(splitStrs2[j])
                j += 1
            if i < len(splitStrs1):
                ans.append(splitStrs1[i].split(':')[1])
            # move onto the next non subsequence char
            i += 1
            j += 1

        while i < len(splitStrs1):
            ans.append(splitStrs1[i])
            i += 1
        while j < len(splitStrs2):
            ans.append(splitStrs2[j])
            j += 1

        return ''.join(ans)

    def splitStringBySubsequence(self, subsequence: str, originalStr: str) -> List[str]:
        j = 0
        splitSubStrs = []
        for char in originalStr:
            if j >= len(subsequence):
                splitSubStrs.append(char)
                continue
            if char == subsequence[j]:
                splitSubStrs.append("subsqs:" + char)
                j += 1
            else:
                splitSubStrs.append(char)

        return splitSubStrs

    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
        m, n = len(text1), len(text2)
        # dp[i][j] stores the LCS between text1[:i] & text2[:j]
        dp = [['' for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + text1[i - 1]
                else:
                    if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]


print(Solution().shortestCommonSupersequence(str1="abac", str2="cab"))
print(Solution().shortestCommonSupersequence(str1="aaaaaaaa", str2="aaaaaaaa"))
