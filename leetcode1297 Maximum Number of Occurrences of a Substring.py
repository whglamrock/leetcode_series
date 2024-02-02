from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subStringToCount = defaultdict(int)
        l = 0
        window = defaultdict(int)
        for r, char in enumerate(s):
            window[char] += 1
            while r - l + 1 > minSize or len(window) > maxLetters:
                window[s[l]] -= 1
                if not window[s[l]]:
                    del window[s[l]]
                l += 1

            if r - l + 1 == minSize:
                subStringToCount[s[l:r + 1]] += 1

        return max(subStringToCount.values()) if subStringToCount else 0
