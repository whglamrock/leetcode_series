from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        m, n = len(s), len(p)
        charCountOfP = Counter(p)
        charCountOfSubStrS = Counter(s[:n])
        ans = []
        if charCountOfP == charCountOfSubStrS:
            ans.append(0)

        for i in range(1, m - n + 1):
            charCountOfSubStrS[s[i - 1]] -= 1
            charCountOfSubStrS[s[i + n - 1]] += 1
            if not charCountOfSubStrS[s[i - 1]]:
                del charCountOfSubStrS[s[i - 1]]
            if charCountOfSubStrS == charCountOfP:
                ans.append(i)

        return ans
