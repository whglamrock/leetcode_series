from math import inf
from typing import List

# greedy approach. Where there is conflict/overlap, always use the interval with the smallest right
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 0
        currRight = -inf
        for left, right in pairs:
            # found a chain
            if left > currRight:
                currRight = right
                ans += 1

        return ans
