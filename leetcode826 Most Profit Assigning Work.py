from heapq import *
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)
        jobs = []
        for i in range(len(difficulty)):
            heappush(jobs, [-profit[i], difficulty[i]])

        maxProfit = 0
        for capability in worker:
            while jobs and jobs[0][1] > capability:
                heappop(jobs)
            if jobs:
                maxProfit += -jobs[0][0]

        return maxProfit
