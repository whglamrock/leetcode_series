from typing import List


# To achieve O(N ^ 2) time, we will have to use DP. The easiest to implement approach is using 4 n^2 dp arrays to store
# the number of consecutive ones at grid[i][j] for each direction.
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1 for j in range(n)] for i in range(n)]
        for i, j in mines:
            grid[i][j] = 0

        left = [[0 for j in range(n)] for i in range(n)]
        right = [[0 for j in range(n)] for i in range(n)]
        up = [[0 for j in range(n)] for i in range(n)]
        down = [[0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    left[i][j] = 0
                else:
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j - 1] + 1
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    right[i][j] = 0
                else:
                    if j == n - 1:
                        right[i][j] = 1
                    else:
                        right[i][j] = right[i][j + 1] + 1

        for j in range(n):
            for i in range(n):
                if grid[i][j] == 0:
                    up[i][j] = 0
                else:
                    if i == 0:
                        up[i][j] = 1
                    else:
                        up[i][j] = up[i - 1][j] + 1
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    down[i][j] = 0
                else:
                    if i == n - 1:
                        down[i][j] = 1
                    else:
                        down[i][j] = down[i + 1][j] + 1

        maxOrder = 0
        for i in range(n):
            for j in range(n):
                currOrder = min(left[i][j], right[i][j], up[i][j], down[i][j])
                maxOrder = max(maxOrder, currOrder)

        return maxOrder


print(Solution().orderOfLargestPlusSign(5, [[4, 2]]))
