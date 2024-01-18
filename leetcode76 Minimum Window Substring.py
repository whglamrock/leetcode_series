from collections import defaultdict, Counter
from typing import Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charCountOfT = Counter(t)
        window = defaultdict(int)
        l = 0
        start, end = None, None
        for r, char in enumerate(s):
            window[char] += 1
            while l <= r and self.areAllCharsIncluded(window, charCountOfT):
                if start is None or r - l + 1 < end - start + 1:
                    start, end = l, r
                window[s[l]] -= 1
                l += 1

        return s[start:end + 1] if start is not None else ''

    # O(1) time because there are at most 52 letters
    def areAllCharsIncluded(self, window: Dict[str, int], charCountOfT: Dict[str, int]):
        for char in charCountOfT:
            if char not in window or window[char] < charCountOfT[char]:
                return False
        return True


print(Solution().minWindow('abbdcecbgaaw', 'abc'))
print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('ADOBECODEBANC', 'ABCC'))
