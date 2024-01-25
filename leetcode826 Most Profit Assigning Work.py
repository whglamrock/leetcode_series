from heapq import *
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        workersWithIndex = []
        for i in range(len(worker)):
            workersWithIndex.append([worker[i], i])
        workersWithIndex.sort(key=lambda x: -x[0])

        pq = []
        for i in range(len(difficulty)):
            heappush(pq, [-profit[i], difficulty[i]])

        ans = 0
        for ability, i in workersWithIndex:
            while pq and pq[0][1] > ability:
                heappop(pq)
            if pq:
                ans += -pq[0][0]

        return ans
