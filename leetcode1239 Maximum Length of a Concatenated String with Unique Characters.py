from collections import Counter
from functools import lru_cache
from typing import List

class Solution:
    def __init__(self):
        self.arr = []

    def maxLength(self, arr: List[str]) -> int:
        deDupedArr = set()
        for word in arr:
            if max(Counter(word).values()) == 1:
                deDupedArr.add(word)
        self.arr = list(deDupedArr)
        return self.dfs(0, '')

    @lru_cache(None)
    def dfs(self, i: int, currSubseq: str) -> int:
        if i >= len(self.arr):
            return len(currSubseq)

        currCharSet = set()
        for char in currSubseq:
            currCharSet.add(char)

        longest = len(currSubseq)
        for j in range(i, len(self.arr)):
            isOverlapping = False
            newCharSet = set()
            for char in self.arr[j]:
                if char in currCharSet:
                    isOverlapping = True
                newCharSet.add(char)

            # can continue from current subsequence
            if not isOverlapping:
                newCharSet = newCharSet.union(currCharSet)

            newSubseq = ''.join(sorted(newCharSet))
            longest = max(longest, self.dfs(j + 1, newSubseq))

        return longest
