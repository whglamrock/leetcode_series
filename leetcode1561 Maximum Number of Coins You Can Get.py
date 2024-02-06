from collections import deque
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))
        ans = 0
        while piles:
            piles.pop()
            ans += piles.pop()
            piles.popleft()

        return ans
