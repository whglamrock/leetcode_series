
# dp idea came from https://leetcode.com/problems/count-substrings-that-differ-by-one-character/solutions/917701/c-java-python3-o-n-3-o-n-2/
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dpl[i][j] means the max length of common substring of s[:i] and t[:j]
        dpl = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dpl[i][j] = 1 + dpl[i - 1][j - 1]

        # dpr[i][j] means the max length of common substring of s[i:] and t[j:]
        dpr = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dpr[i - 1][j - 1] = dpr[i][j] + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    ans += (dpl[i][j] + 1) * (dpr[i + 1][j + 1] + 1)

        return ans
