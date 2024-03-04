from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        basket = defaultdict(int)
        l = 0
        for r, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if not basket[fruits[l]]:
                    del basket[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)

        return ans


print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
