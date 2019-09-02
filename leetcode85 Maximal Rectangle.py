
# a typical multi-dpArray dp question. In this question, we could also use 2-D array for left, right, height but
    # 1-D takes less space
# explanation from: https://discuss.leetcode.com/topic/6650/share-my-dp-solution

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # left[j] stores the left most index k that all left[k:j + 1] is 1
        left = [0] * n
        # right[j] stores the right most index k that all right[j:k + 1] is 1
        right = [n] * n
        height = [0] * n

        maxArea = 0
        for i in xrange(m):
            currLeft, currRight = 0, n
            for j in xrange(n):
                if matrix[i][j] == '1':
                    # 1. not making left[j] directly = currLeft because currLeft only means the leftmost consecutive 1
                        # and the corresponding height[currLeft] is very possibly different
                    # 2. the previous left[j] represents that with the previous height[i], how left we can go
                    # 3. the currLeft only records for the current row
                    left[j] = max(left[j], currLeft)
                else:
                    currLeft = j + 1
                    # reset it 0 is for the next big for loop (i + 1)
                    # this won't affect the area calculation because the corresponding
                    # height[j] will be 0
                    left[j] = 0

            for j in xrange(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], currRight)
                else:
                    # notice that we make currRight = j instead of j - 1 to ease the area calculation
                    currRight = j
                    # reset it n is for the next big for loop (i + 1)
                    right[j] = n

            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in xrange(n):
                # no need to do right[j] - left[j] "+ 1" because right[j] stores the index + 1
                maxArea = max(maxArea, (right[j] - left[j]) * height[j])

        return maxArea



matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print Solution().maximalRectangle(matrix)

