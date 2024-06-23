from functools import lru_cache


class Solution:
    def minTimeToType(self, word: str) -> int:
        minTime = len(word)
        prevChar = 'a'
        for i in range(len(word)):
            currChar = word[i]
            minTime += self.calculateDistance(prevChar, currChar)
            prevChar = currChar

        return minTime

    @lru_cache(None)
    def calculateDistance(self, char1: str, char2: str) -> int:
        dist = abs(ord(char2) - ord(char1))
        reverseDist = 26 - dist
        return min(dist, reverseDist)
