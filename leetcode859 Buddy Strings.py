from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sCounter = Counter(s)
        if len(s) < 2 or sCounter != Counter(goal):
            return False

        numOfDifferentChars = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                numOfDifferentChars += 1
            if numOfDifferentChars > 2:
                return False

        # numOfDifferentChars can only be 2 or 0
        return numOfDifferentChars == 2 or max(sCounter.values()) >= 2
