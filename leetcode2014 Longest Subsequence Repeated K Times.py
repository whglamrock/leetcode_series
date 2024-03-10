from collections import Counter
from itertools import combinations, permutations

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # the char needs to time a frequency // k because if a char can be used for x times
        # in the subsequence if it appears more than x * k times
        hotChars = "".join(char * (count // k) for char, count in Counter(s).items())
        combinationSet = set()
        for length in range(len(hotChars) + 1):
            for combination in combinations(hotChars, length):
                for permutation in permutations(combination):
                    combinationSet.add(''.join(permutation))

        combinationSet = sorted(combinationSet, key=lambda x: (len(x), x), reverse=True)
        for combination in combinationSet:
            if self.isSubsequence(s, combination, k):
                return combination

    def isSubsequence(self, s: str, substr: str, k) -> bool:
        substr = substr * k
        i, j = 0, 0
        m, n = len(s), len(substr)
        if len(s) < len(substr):
            return False

        while i < m and j < n:
            if s[i] == substr[j]:
                i += 1
                j += 1
            else:
                i += 1

        return j == n
