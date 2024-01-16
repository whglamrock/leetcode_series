from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > currMin:
                ans += prices[i] - currMin
            currMin = prices[i]

        return ans


print(Solution().maxProfit([1, 4, 5, 2, 9, 16]))
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
