from typing import List

# The greedy idea is: for the current balloon i, try to find all balloons on the right that overlap with it. We need
# to sort by the end not the start of the interval because otherwise there could be some balloons j & k which all overlap
# with i but j & k don't overlap, in which case we cannot burst i, j, k with one arrow.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        i, n = 0, len(points)
        points.sort(key=lambda x: x[1])
        while i < n:
            ans += 1
            j = i
            while j < n and points[j][0] <= points[i][1]:
                j += 1
            i = j

        return ans


print(Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
