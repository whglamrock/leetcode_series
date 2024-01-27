from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        for i, h in enumerate(height):
            # when prevH == h we still need to pop.
            # e.g., consider edge case like [5, 2, 1, 2, 1, 5]
            while stack and stack[-1][1] <= h:
                prevI, prevH = stack.pop()
                if stack:
                    area += (i - stack[-1][0] - 1) * (min(h, stack[-1][1]) - prevH)
            stack.append([i, h])

        return area


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
print(Solution().trap([0, 1, 0, 3, 1, 0, 3, 4, 2, 1, 3, 1]))
# if we use while stack and stack[-1][1] < h, below will yield wrong answer 16
print(Solution().trap([5, 2, 1, 2, 1, 5]))
