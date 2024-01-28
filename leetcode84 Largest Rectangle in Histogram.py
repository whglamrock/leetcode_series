from typing import List

# remember the trick of pre-adding [-1, 0] to the stack because we need to use
# i - stack[-1][0] - 1 to as the bottom to calculate the area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[-1, 0]]
        maxArea = 0
        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                j, prevH = stack.pop()
                maxArea = max(maxArea, prevH * (i - stack[-1][0] - 1))
            stack.append([i, h])

        while stack:
            i, h = stack.pop()
            if stack:
                maxArea = max(maxArea, h * (len(heights) - stack[-1][0] - 1))

        return maxArea


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
