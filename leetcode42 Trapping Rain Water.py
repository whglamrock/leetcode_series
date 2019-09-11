
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
        if not height or len(height) <= 2:
            return 0

        stack = []
        accum = 0
        ans = 0
        for i in xrange(len(height)):
            if not stack:
                stack.append([i, height[i]])
            elif stack[-1][-1] == height[i]:
                stack.pop()
                stack.append([i, height[i]])
            elif stack[-1][-1] > height[i]:
                stack.append([i, height[i]])
            else:
                while stack and stack[-1][-1] < height[i]:
                    j, lastHeight = stack.pop()
                    if not stack:
                        break
                    accum += (min(height[i], stack[-1][-1]) - lastHeight) * (i - stack[-1][0] - 1)

                ans += accum
                accum = 0
                stack.append([i, height[i]])

        return ans



print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])