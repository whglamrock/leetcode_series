from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, height in enumerate(heights):
            while stack and stack[-1][1] <= height:
                j, previousHeight = stack.pop()
                if previousHeight == height:
                    stack.append([i, height])
                    break
                # previous height < height so j can be bottom
                if stack:
                    area += (i - stack[-1][0] - 1) * (min(height, stack[-1][1]) - previousHeight)
            stack.append([i, height])

        return area


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
print(Solution().trap([0, 1, 0, 3, 1, 0, 3, 4, 2, 1, 3, 1]))
