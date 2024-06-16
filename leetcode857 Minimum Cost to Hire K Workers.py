from heapq import *
from typing import List


# see explanation from: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solutions/141768/detailed-explanation-o-nlogn/
# in this find k optimal question: there are 2 variables: ratio and quality. You want k workers with lowest
# ratio (wage/quality) and lowest quality, in order to form a lowest paid group. But the group's ratio is decided
# by the highest ratio within the group. A typical solution for this type of question is sorting + heapq.
class Solution:
    def mincostToHireWorkers(self, qualities: List[int], wages: List[int], k: int) -> float:
        workers = []
        for quality, wage in zip(qualities, wages):
            workers.append([wage / quality, quality, wage])
        workers.sort()

        workerPq = []
        qualitySum = 0
        minWage = 2147483647
        for i in range(len(workers)):
            if len(workerPq) == k:
                prevQuality, prevWage = heappop(workerPq)
                prevQuality, prevWage = -prevQuality, -prevWage
                qualitySum -= prevQuality
            ratio, quality, wage = workers[i]
            qualitySum += quality
            heappush(workerPq, [-quality, -wage])

            if len(workerPq) == k:
                minWage = min(minWage, qualitySum * ratio)

        return minWage
