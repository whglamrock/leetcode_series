from heapq import *
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        pq = []
        for i in range(len(dist)):
            heappush(pq, [dist[i] / speed[i], dist[i], speed[i]])

        numOfMonsters = 0
        while pq and pq[0][0] > numOfMonsters:
            numOfMonsters += 1
            heappop(pq)

        return numOfMonsters
