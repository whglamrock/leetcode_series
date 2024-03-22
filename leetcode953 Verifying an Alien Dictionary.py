from typing import Tuple, List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienCharToIndex = {}
        for i, char in enumerate(order):
            alienCharToIndex[char] = i

        n = len(words)
        for i in range(n - 1):
            word1, word2 = words[i], words[i + 1]
            if word1 == word2 or (word2.startswith(word1) and len(word2) > len(word1)):
                continue
            if word1.startswith(word2) and len(word1) > len(word2):
                return False
            char1, char2 = self.findFirstDiffCharPair(word1, word2)
            if alienCharToIndex[char1] > alienCharToIndex[char2]:
                return False

        return True

    # it's assumed word1 and word2 don't completely overlap
    def findFirstDiffCharPair(self, word1: str, word2: str) -> Tuple[str, str]:
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return word1[i], word2[i]
