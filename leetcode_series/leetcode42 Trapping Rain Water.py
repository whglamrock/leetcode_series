
# the key is to find how to calculate the accum. Drawing a picture helps.
# Another important idea: once we accumulate the water trapped, we treat it as
# concrete bars (trap the water and "fill" it with concrete).

class Solution(object):
    def trap(self, height):

        stack = []
        accum = 0
        ans = 0
        for i in xrange(len(height)):
            if not stack:
                stack.append([i, height[i]])
            else:
                if height[i] < stack[-1][-1]:
                    stack.append([i, height[i]])
                elif height[i] == stack[-1][-1]:
                    stack.pop()
                    stack.append([i, height[i]])
                else:
                    while stack and stack[-1][-1] < height[i]:
                        j, lastheight = stack.pop()
                        if not stack:
                            continue
                        accum += (min(height[i], stack[-1][-1]) - lastheight) * (i - stack[-1][0] - 1)
                        #print accum, stack
                    ans += accum
                    accum = 0
                    stack.append([i, height[i]])

        return ans