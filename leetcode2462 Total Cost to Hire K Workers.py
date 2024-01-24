from heapq import *
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        rightIndexOfLeft, leftIndexOfRight = 0, len(costs) - 1
        leftPq, rightPq = [], []
        visited = set()
        while len(leftPq) < candidates:
            heappush(leftPq, [costs[rightIndexOfLeft], rightIndexOfLeft])
            visited.add(rightIndexOfLeft)
            rightIndexOfLeft += 1
        while len(rightPq) < candidates:
            if leftIndexOfRight in visited:
                break
            heappush(rightPq, [costs[leftIndexOfRight], leftIndexOfRight])
            visited.add(leftIndexOfRight)
            leftIndexOfRight -= 1

        totalCost = 0
        for _ in range(k):
            # leftPq and rightPq can't be both empty
            if not leftPq or (rightPq and leftPq[0][0] > rightPq[0][0]):
                minCost, index = heappop(rightPq)
                if leftIndexOfRight >= 0 and leftIndexOfRight not in visited:
                    heappush(rightPq, [costs[leftIndexOfRight], leftIndexOfRight])
                    visited.add(leftIndexOfRight)
                    leftIndexOfRight -= 1
            else:
                minCost, index = heappop(leftPq)
                if rightIndexOfLeft < len(costs) and rightIndexOfLeft not in visited:
                    heappush(leftPq, [costs[rightIndexOfLeft], rightIndexOfLeft])
                    visited.add(rightIndexOfLeft)
                    rightIndexOfLeft += 1

            totalCost += minCost

        return totalCost


print(Solution().totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
print(Solution().totalCost(costs=[1, 2, 4, 1], k=3, candidates=3))
