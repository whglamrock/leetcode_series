from heapq import *
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heappush(pq, -stone)

        while len(pq) >= 2:
            heaviest = -heappop(pq)
            secondHeaviest = -heappop(pq)
            if heaviest > secondHeaviest:
                heappush(pq, secondHeaviest - heaviest)

        return -pq[0] if pq else 0
