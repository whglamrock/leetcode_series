from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1CharCount = Counter(s1)

        l = 0
        window = defaultdict(int)
        for r, char in enumerate(s2):
            window[char] += 1
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if not window[s2[l]]:
                    del window[s2[l]]
                l += 1
            if window == s1CharCount:
                return True

        return False
