from heapq import *
from math import sqrt
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            dist = sqrt(x * x + y * y)
            heappush(pq, [-dist, x, y])
            if len(pq) > k:
                heappop(pq)

        ans = []
        for dist, x, y in pq:
            ans.append([x, y])
        return ans


print(Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4], [4, 2], [2, 0]], K=3))
