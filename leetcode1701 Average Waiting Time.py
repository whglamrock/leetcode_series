from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime = 0
        totalWait = 0

        for i, customer in enumerate(customers):
            startTime, timeNeeded = customer
            if currTime <= startTime:
                totalWait += timeNeeded
                currTime = startTime + timeNeeded
            else:
                totalWait += currTime - startTime + timeNeeded
                currTime = currTime + timeNeeded

        return totalWait / len(customers)
