# see explanation from: http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

# The idea is:
# 1) Use every height[i] as the shortest height and find the left & right index.
# 2) To easily find the left index, we keep an increasing stack; for every popped height[j], the left index
# is stack[-1] and the right index is i (both left & right index are exclusive).
# 3) currArea = height[j] * (i - stack[-1] - 1).
# 4) for corner case, we can consider -1, n as two outer indices and their heights to be 0

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        n = len(heights)
        i = 0
        stack = []
        maxArea = 0

        while i < n:
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                # at this point heights[j] is taller than heights[i] and heights[stack[-1]]
                j = stack.pop()
                if stack:
                    currArea = heights[j] * (i - stack[-1] - 1)
                else:
                    # means heights[j] is currently the shortest in heights[:i]
                    currArea = heights[j] * i
                maxArea = max(maxArea, currArea)

        while stack:
            j = stack.pop()
            if stack:
                currArea = heights[j] * (n - stack[-1] - 1)
            else:
                # heights[j] is the shortest of all heights
                currArea = heights[j] * n
            maxArea = max(maxArea, currArea)

        return maxArea


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
