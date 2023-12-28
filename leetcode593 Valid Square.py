import math
from typing import List, Tuple

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pointsSet = set()
        for p in [p1, p2, p3, p4]:
            pointsSet.add((p[0], p[1]))
        if len(pointsSet) != 4:
            return False

        points = list(pointsSet)
        distances = set()
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                distances.add(self.getDistance(points[i], points[j]))

        return len(distances) == 2

    def getDistance(self, p1: Tuple[int, ...], p2: Tuple[int, ...]) -> float:
        squareSum = (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])
        return math.sqrt(squareSum)


print(Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
print(Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 12]))
print(Solution().validSquare(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1]))
