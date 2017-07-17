
# idea: dp.
# explanation from: https://discuss.leetcode.com/topic/6650/share-my-dp-solution

class Solution(object):
    def maximalRectangle(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # instead of using 2-D arrays, using 1-D to save space
        left = [0] * n
        right = [n] * n
        height = [0] * n
        maxarea = 0

        for i in xrange(m):
            currleft, currright = 0, n
            # update the left, based on the previous and current row
            for j in xrange(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], currleft)
                else:
                    currleft = j + 1    # make it the next j
                    left[j] = 0    # make it zero so the max operator can work
            # update the right
            for j in xrange(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], currright)
                else:
                    currright = j  # not j - 1, for the convenience to calculate right[j] - left[j]
                    right[j] = n    # make it back to n so the min operator can work
            # P.S. we don't have to worry about having wrong result of rectangle's area because when
            #   matrix[i][j] == '0', the height[j] will be set 0
            # update the height
            for j in xrange(n):
                if matrix[i][j] == '1':
                    # based on the previous row's height[j], even if it's 0
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
            # calculate the max area
            for j in xrange(n):
                maxarea = max(maxarea, (right[j] - left[j]) * height[j])

        return maxarea
