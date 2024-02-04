from functools import lru_cache
from typing import List

class Solution:
    def __init__(self):
        self.prefixSum = []
        self.piles = []

    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        self.prefixSum = []
        for i, pile in enumerate(piles):
            if not self.prefixSum:
                self.prefixSum.append(pile)
            else:
                self.prefixSum.append(self.prefixSum[-1] + pile)

        return self.dfs(0, 1, True)

    @lru_cache(None)
    def dfs(self, i: int, m: int, isAlicesTurn: bool) -> int:
        if i >= len(self.piles):
            return 0

        if isAlicesTurn:
            maxStone = 0
            for j in range(i, min(len(self.piles), i + 2 * m)):
                if i == 0:
                    stonesTaken = self.prefixSum[j]
                else:
                    stonesTaken = self.prefixSum[j] - self.prefixSum[i - 1]
                newM = max(m, j - i + 1)
                maxStone = max(maxStone, stonesTaken + self.dfs(j + 1, newM, False))
            return maxStone
        else:
            minStone = 2147483647
            for j in range(i, min(len(self.piles), i + 2 * m)):
                newM = max(m, j - i + 1)
                minStone = min(minStone, self.dfs(j + 1, newM, True))
            return minStone
