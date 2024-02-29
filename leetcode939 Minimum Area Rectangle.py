from collections import defaultdict
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        yPairToXs = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 or y1 == y2:
                    continue
                yPair = (min(y1, y2), max(y1, y2))
                if yPair in yPairToXs and yPairToXs[yPair][-1] == x1:
                    continue
                yPairToXs[yPair].append(x1)

        minArea = 2147483647
        for yPair in yPairToXs:
            y1, y2 = yPair[0], yPair[1]
            # xs is a sorted list of x coordinates
            xs = yPairToXs[yPair]
            for i in range(1, len(xs)):
                x1, x2 = xs[i - 1], xs[i]
                minArea = min(minArea, (x2 - x1) * (y2 - y1))

        return minArea if minArea != 2147483647 else 0
