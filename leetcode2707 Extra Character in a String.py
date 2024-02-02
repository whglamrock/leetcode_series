from functools import lru_cache
from typing import List

# the "dp" solution in leetcode discussion is actually dfs.
class Solution:
    def __init__(self):
        self.dictionary = set()

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.dictionary = set(dictionary)
        return self.dfs(s)

    @lru_cache(None)
    def dfs(self, s: str) -> int:
        if not s or s in self.dictionary:
            return 0

        minCharsToRemove = len(s)
        # choose to remove char
        minCharsToRemove = min(minCharsToRemove, 1 + self.dfs(s[1:]))
        # or find any prefix match
        for i in range(1, len(s)):
            if s[:i] in self.dictionary:
                minCharsToRemove = min(minCharsToRemove, self.dfs(s[i:]))
        return minCharsToRemove

