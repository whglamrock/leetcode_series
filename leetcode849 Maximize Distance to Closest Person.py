from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        indexToClosestLeft = {}
        closestLeft = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                closestLeft = i
            indexToClosestLeft[i] = closestLeft
        n = len(seats)
        indexToClosestRight = {}
        closestRight = -1
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                closestRight = i
            indexToClosestRight[i] = closestRight

        dist = [0] * n
        for i in range(n):
            if seats[i] == 1:
                continue
            if indexToClosestLeft[i] == -1:
                dist[i] = abs(indexToClosestRight[i] - i)
            elif indexToClosestRight[i] == -1:
                dist[i] = abs(indexToClosestLeft[i] - i)
            else:
                dist[i] = min(abs(i - indexToClosestLeft[i]), abs(i - indexToClosestRight[i]))

        return max(dist)

