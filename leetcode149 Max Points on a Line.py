from collections import defaultdict
from math import inf
from typing import List, Tuple

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        parameterToPoints = defaultdict(set)
        for point1 in points:
            for point2 in points:
                if point1 == point2:
                    continue
                k, b = self.calculateParameters(point1, point2)
                parameterToPoints[(k, b)].add((point1[0], point1[1]))
                parameterToPoints[(k, b)].add((point2[0], point2[1]))
        return max(len(numOfPoints) for numOfPoints in parameterToPoints.values())

    def calculateParameters(self, point1: List[int], point2: List[int]) -> Tuple[int, int]:
        x1, y1 = point1
        x2, y2 = point2
        if x1 == x2:
            k = inf
        else:
            k = (y2 - y1) / (x2 - x1)
        # when slope is infinite just use x1 to identify this line
        b = y1 - k * x1 if k != inf else x1
        return k, b


print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
# this leetcode test case is really stupid!
print(Solution().maxPoints([[0, 0], [94911151, 94911150], [94911152, 94911151]]))
