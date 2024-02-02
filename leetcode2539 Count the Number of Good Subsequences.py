from collections import defaultdict
from functools import lru_cache
from typing import Dict

# A stupid, meaningless math problem. The stupid leetcode should categorize is as hard, not medium
# The below solution fot TLE in fucking leetcode but is definitely acceptable in real interview.
class Solution:
    def __init__(self):
        self.numOfCombinations = {}

    def countGoodSubsequences(self, s: str) -> int:
        prefixCharCount = defaultdict(int)
        ans, mod = 0, 10 ** 9 + 7
        self.numOfCombinations = {}

        for char in s:
            prefixCharCount[char] += 1
            for i in range(1, prefixCharCount[char] + 1):
                ans += self.generateNumOfGoodSeqs(prefixCharCount, i, char)
                ans %= mod

        return ans

    def generateNumOfGoodSeqs(self, prefixCharCount: Dict[str, int], i: int, currChar: str) -> int:
        ans = 1
        for char in prefixCharCount:
            if prefixCharCount[char] < i:
                continue
            if char != currChar:
                # the extra + 1 is for not choosing the char at all
                ans *= self.numOfCombination(prefixCharCount[char], i) + 1
            else:
                ans *= self.numOfCombination(prefixCharCount[char] - 1, i - 1)

        return ans

    @lru_cache(None)
    def numOfCombination(self, limit: int, numOfElements: int):
        if (limit - 1, numOfElements) in self.numOfCombinations:
            return self.numOfCombinations[(limit - 1, numOfElements)] * limit // (limit - numOfElements)
        if (limit, numOfElements - 1) in self.numOfCombinations:
            return self.numOfCombinations[(limit, numOfElements - 1)] * (limit - numOfElements + 1) // numOfElements

        denominator = 1
        for j in range(limit, limit - numOfElements, -1):
            denominator *= j
        numerator = 1
        for k in range(1, numOfElements + 1):
            numerator *= k

        self.numOfCombinations[(limit, numOfElements)] = denominator // numerator
        return denominator // numerator
