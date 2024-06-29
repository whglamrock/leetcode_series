from typing import List


# the only reason this question is hard is because it forces you to use KMP/rolling hash, otherwise you get TLE.
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
            dp = [0] * len(s)
            for i in range(1, len(s)):
                curr = dp[i - 1]
                while curr and s[i] != s[curr]:
                    curr = dp[curr - 1]
                dp[i] = curr + (s[i] == s[curr])
            return dp

        n, la, lb = len(s), len(a), len(b)
        v1 = kmp(a + '#' + s)
        v2 = kmp(b + '#' + s)
        ii = [i - la - la for i, v in enumerate(v1) if v >= la]
        jj = [j - lb - lb for j, v in enumerate(v2) if v >= lb]
        res = []
        j = 0
        for i in ii:
            while j < len(jj) and jj[j] < i - k:
                j += 1
            if j < len(jj) and jj[j] <= i + k:
                res.append(i)

        return res
