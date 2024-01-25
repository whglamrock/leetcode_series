from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False

        numOfDifferentChars = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                numOfDifferentChars += 1
            if numOfDifferentChars > 2:
                return False

        return True
