from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordCount = Counter(words)
        visited = set()
        ans = 0
        isCenterUsed = False
        for word, count in wordCount.items():
            if word in visited:
                continue
            visited.add(word)
            reverseWord = word[::-1]
            # can be center
            if word == reverseWord:
                if count % 2:
                    if not isCenterUsed:
                        ans += count * 2
                        isCenterUsed = True
                    else:
                        ans += (count - 1) * 2
                else:
                    ans += count * 2
            else:
                if reverseWord in wordCount:
                    visited.add(reverseWord)
                    ans += min(count, wordCount[reverseWord]) * 4

        return ans
