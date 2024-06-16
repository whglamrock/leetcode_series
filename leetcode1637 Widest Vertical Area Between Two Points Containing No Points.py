from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        maxWidth = 0
        for i in range(len(points) - 1):
            currX, nextX = points[i][0], points[i + 1][0]
            if currX == nextX:
                continue
            maxWidth = max(maxWidth, nextX - currX)

        return maxWidth
