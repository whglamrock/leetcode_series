
# see explanation from: http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

class Solution(object):
    def largestRectangleArea(self, heights):

        if not heights:
            return 0

        # ensure the heights in stack are in sorted order
        stack = []
        maxarea = 0
        i = 0
        n = len(heights)

        while i < n:
            # applies to the case when heights[i] == 0
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            # when theindexofminheight != i - 1, all bars between them are guaranteed no shorter than theindexofminheight
            else:
                # get the index of bar that's used as the height of the rec (shortest among current bars)
                theindexofminheight = stack.pop()
                currarea = 0
                # the right bound of the rectangle is i - 1, the left bound is stack[-1] + 1
                if stack:
                    # theindexofminheight doesn't necessarily == the current stack[-1] + 1,
                    #   just like when theindexofminheight != i - 1, but all bars between them
                    #   are guaranteed no shorter than theindexofminheight
                    currarea = heights[theindexofminheight] * (i - stack[-1] - 1)
                # in this case, the left bound is 0, no bars from 0 to theindexofminheight are taller
                else:
                    currarea = heights[theindexofminheight] * i
                maxarea = max(maxarea, currarea)

        # likewise
        while stack:
            theindexofminheight = stack.pop()
            currarea = 0
            if stack:
                currarea = heights[theindexofminheight] * (n - stack[-1] - 1)
            else:
                currarea = heights[theindexofminheight] * n
            maxarea = max(maxarea, currarea)

        return maxarea