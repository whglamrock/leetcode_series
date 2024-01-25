from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDistance = 2147483648
        ans = -1
        for i in range(len(points)):
            xx, yy = points[i][0], points[i][1]
            if xx != x and yy != y:
                continue
            distance = abs(xx - x) + abs(yy - y)
            if distance < minDistance:
                minDistance = distance
                ans = i

        return ans
