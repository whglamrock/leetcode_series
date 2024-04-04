from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        window = defaultdict(list)
        for r, char in enumerate(word):
            if char not in 'aeiou':
                window = defaultdict(list)
                continue

            window[char].append(r)
            if len(window) == 5:
                minLeftBound, maxLeftBound = window[char][0], window[char][-1]
                for vowel in window:
                    minLeftBound = min(minLeftBound, window[vowel][0])
                    maxLeftBound = min(maxLeftBound, window[vowel][-1])
                ans += maxLeftBound - minLeftBound + 1

        return ans
