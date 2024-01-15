from typing import List

# see real explanation: https://leetcode.com/problems/container-with-most-water/solutions/6100/simple-and-clear-proof-explanation/comments/880632
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxAmountOfWater = 0
        while l < r:
            maxAmountOfWater = max(maxAmountOfWater, (r - l) * min(height[l], height[r]))
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1

        return maxAmountOfWater


print(Solution().maxArea([1, 2, 3, 12, 1, 2, 14, 8]))
# tricky test case:
print(Solution().maxArea([1, 3, 2, 5, 25, 24, 5]))
