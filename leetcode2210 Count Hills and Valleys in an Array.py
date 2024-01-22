from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        heights = []
        for num in nums:
            if not heights or heights[-1] != num:
                heights.append(num)

        count = 0
        for i in range(1, len(heights) - 1):
            if heights[i - 1] < heights[i] > heights[i + 1] or heights[i - 1] > heights[i] < heights[i + 1]:
                count += 1

        return count


print(Solution().countHillValley([6, 6, 5, 5, 4, 1]))
print(Solution().countHillValley([2, 4, 1, 1, 6, 5]))
