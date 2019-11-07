
# It's natural to think of decreasing stack solution. The key is to avoid combining with previous bars
# e.g., in test case [0, 1, 0, 2, (1, 0, 1), 3, 2, 1, 2, 1], we need to deal with the 3 bars within parentheses;
    # we don't need to combine heights/add popped height back, because "min(height[i], stack[-1][-1]) - lastHeight"
    # will prevent double adding trapped water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        stack = []
        ans = 0

        for i, h in enumerate(height):
            if not stack or h < stack[-1][1]:
                stack.append([i, h])
                continue
            while stack and h >= stack[-1][1]:
                lastH = stack.pop()[1]
                if stack:
                    heightDiff = min(h, stack[-1][1]) - lastH
                    ans += heightDiff * (i - stack[-1][0] - 1)
            stack.append([i, h])

        return ans



print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])