from collections import defaultdict, Counter
from typing import Dict

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 1:
            return s == goal
        if len(s) == 2:
            return s == goal or s == goal[::-1]
        if Counter(s) != Counter(goal):
            return False

        charToNeighborsOfS = self.generateCharToNeighbors(s)
        charToNeighborsOfGoal = self.generateCharToNeighbors(goal)
        return charToNeighborsOfS == charToNeighborsOfGoal

    def generateCharToNeighbors(self, s: str) -> Dict[str, set]:
        charToNeighbors = defaultdict(set)
        for i, char in enumerate(s):
            if i == 0:
                left, right = s[i + 1], s[-1]
            elif i == len(s) - 1:
                left, right = s[i - 1], s[0]
            else:
                left, right = s[i + 1], s[i - 1]
            left, right = sorted([left, right])[0], sorted([left, right])[1]
            charToNeighbors[char].add((left, right))
        return charToNeighbors
