from math import inf
from collections import defaultdict, Counter
from typing import Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charCountOfT = Counter(t)
        window = defaultdict(int)
        l = 0
        minLen = 2147483647
        start, end = -inf, inf

        for r, char in enumerate(s):
            window[char] += 1
            while l <= r and (s[l] not in charCountOfT or window[s[l]] > charCountOfT[s[l]]):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            if self.areAllCharsIncluded(window, charCountOfT):
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    start, end = l, r

        return s[start:end + 1] if minLen != 2147483647 else ''

    # O(1) time because there are at most 52 chars
    def areAllCharsIncluded(self, window: Dict[str, int], charCountOfT: Dict[str, int]) -> bool:
        if len(window) < len(charCountOfT):
            return False
        for char in charCountOfT:
            if char not in window or window[char] < charCountOfT[char]:
                return False
        return True


print(Solution().minWindow('abbdcecbgaaw', 'abc'))
print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('ADOBECODEBANC', 'ABCC'))
