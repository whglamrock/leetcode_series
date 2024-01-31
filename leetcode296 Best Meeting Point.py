from typing import List

# The hard part is to be able to think of the idea meeting point is the median of all x/y coordinates:
# 1) Assuming you have even number of coordinates x1, x2, ... xi,...xn, and xi is the n/2'th element.
# 2) There is a range [x_left, x_right] where the number of coordinates < x_left == the number of coordinates > x_right,
# you can tell that no matter how you move xi within the range, it doesn't change the total distance between xi and
# all coordinates outside the range.
# 3) But for coordinates within [x_left, x_right], the best point is xi == (x_left, x_right) / 2 because any other xi
# position will make the total distance between xi and other coordinates within [x_left, x_right] bigger.
# 4) Thus, the overall best meeting point is the median of all x/y coordinates (since indexes are all integers)
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        x, y = rows[len(rows) // 2], cols[len(cols) // 2]
        totalDistance = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    totalDistance += abs(x - i) + abs(y - j)
        return totalDistance


print(Solution().minTotalDistance([
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]]))
