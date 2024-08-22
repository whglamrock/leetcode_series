class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        m, n = len(s), len(t)
        while j < n:
            if i >= m:
                break

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                while j < n and t[j] != s[i]:
                    j += 1

        return i == m
