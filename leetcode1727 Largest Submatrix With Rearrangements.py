from typing import List

# 1) Within each row i, consider matrix[0][j] to matrix[i][j] a pillar that forms a rectangle.
# 2) If there's 0 in it, then the pillar is broken but we can calculate the height of the pillar[j] with matrix[i][j]
# as its bottom if matrix[i][j] == 1, else pillar[j] = 0
# 3) sort the pillar array of each row, then iterate the pillar array from left to right and calculate the max area
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        heights = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            sortedHeights = sorted(heights)
            for j in range(n):
                ans = max(ans, sortedHeights[j] * (n - j))

        return ans
