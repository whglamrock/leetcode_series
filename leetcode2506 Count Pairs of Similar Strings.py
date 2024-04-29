from collections import defaultdict
from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sortedCharSetToIndexes = defaultdict(list)
        for i, word in enumerate(words):
            sortedCharSet = self.getSortedChars(word)
            sortedCharSetToIndexes[sortedCharSet].append(i)

        ans = 0
        for indexes in sortedCharSetToIndexes.values():
            if len(indexes) >= 2:
                ans += len(indexes) * (len(indexes) - 1) // 2

        return ans

    def getSortedChars(self, word: str) -> str:
        charSet = set(word)
        return ''.join(sorted(charSet))
