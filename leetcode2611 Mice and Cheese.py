from heapq import *
from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        pq = []
        totalPointsFor2 = 0
        for point1, point2 in list(zip(reward1, reward2)):
            heappush(pq, [point1 - point2, point1, point2])
            if len(pq) > k:
                totalPointsFor2 += heappop(pq)[2]

        return sum(item[1] for item in pq) + totalPointsFor2
