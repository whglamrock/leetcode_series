
# idea: dp.
# explanation from: https://discuss.leetcode.com/topic/6650/share-my-dp-solution

class Solution(object):
    def maximalRectangle(self, matrix):

        if (not matrix) or (not matrix[0]):
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0 for i in xrange(n)]
        right = [n for i in xrange(n)]
        height = [0 for i in xrange(n)]
        maxA = 0

        for i in xrange(m):
            curleft = 0
            curright = n
            for j in xrange(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curleft)
                else:
                    curleft = j + 1
                    # it's necessary to update the left[j], because if we don't update,
                    # the 'max(left[j], curleft)' could yield wrong answer.
                    left[j] = 0

            for j in xrange(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curright)
                else:
                    curright = j
                    # likewise, right[j] also needs to be updated
                    right[j] = n

            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in xrange(n):
                maxA = max(maxA, (right[j] - left[j]) * height[j])

        return maxA