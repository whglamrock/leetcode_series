from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNumOfCandies = max(candies)
        n = len(candies)
        ans = [False] * n
        for i, candy in enumerate(candies):
            if candy + extraCandies >= maxNumOfCandies:
                ans[i] = True
        return ans
