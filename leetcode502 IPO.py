from heapq import *
from typing import List


# P.S.: when we complete a project we don't have to deduct the capital from the total amount. The "capital" here in
# in the question is not the cost!
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        benefits = sorted(zip(profits, capital), key=lambda x: x[1])
        pq = []

        j = 0
        for _ in range(k):
            while j < n and benefits[j][1] <= w:
                heappush(pq, -benefits[j][0])
                j += 1
            if pq:
                w += -heappop(pq)
            else:
                break

        return w


print(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
