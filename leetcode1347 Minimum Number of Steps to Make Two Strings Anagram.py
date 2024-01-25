from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter, tCounter = Counter(s), Counter(t)
        ans = 0
        for char in sCounter:
            if sCounter[char] > tCounter[char]:
                ans += sCounter[char] - tCounter[char]
        return ans
