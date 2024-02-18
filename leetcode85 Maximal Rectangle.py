from typing import List

# The idea comes from lc84: Largest Rectangle in Histogram.
# 1) We consider consecutive 1's in each row as "pillar" to form part of the rectangle
# 2) Keep a heights array when we loop through each row. If any element is 0 the height of the pillar becomes 0
# 3) Then within each row, we have a heights aray, this becomes the Largest Rectangle in Histogram problem
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1

            # increasing stack
            stack = [[-1, 0]]
            for j, h in enumerate(heights):
                while stack and h < stack[-1][1]:
                    prevIndex, prevH = stack.pop()
                    maxArea = max(maxArea, prevH * (j - stack[-1][0] - 1))
                stack.append([j, h])
            while stack:
                prevIndex, prevH = stack.pop()
                if stack:
                    maxArea = max(maxArea, prevH * (n - stack[-1][0] - 1))

        return maxArea


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(Solution().maximalRectangle(matrix))
