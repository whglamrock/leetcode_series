from math import inf
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0] == coordinates[1][0]:
            k = inf
        elif coordinates[0][1] == coordinates[1][1]:
            k = 0
        else:
            k = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])

        for x, y in coordinates[2:]:
            if k == inf:
                if x != coordinates[0][0]:
                    return False
            elif k == 0:
                if y != coordinates[0][1]:
                    return False
            else:
                # avoid 0 division
                if x == coordinates[0][0]:
                    return False
                kk = (y - coordinates[0][1]) / (x - coordinates[0][0])
                if kk != k:
                    return False

        return True
