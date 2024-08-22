from functools import lru_cache
from typing import List


# O(n) solution with visited set and lru cache. Note that we still need the visited with cache to avoid infinite jump
class Solution:
    def __init__(self):
        self.visited = set()
        self.arr = []

    def canReach(self, arr: List[int], start: int) -> bool:
        self.arr = arr
        self.visited = set()
        return self.dfs(start)

    @lru_cache(None)
    def dfs(self, i: int) -> bool:
        if self.arr[i] == 0:
            return True

        if i in self.visited:
            return False
        self.visited.add(i)

        canReach0 = False
        if i + self.arr[i] < len(self.arr):
            canReach0 |= self.dfs(i + self.arr[i])
        if i - self.arr[i] >= 0:
            canReach0 |= self.dfs(i - self.arr[i])

        return canReach0
