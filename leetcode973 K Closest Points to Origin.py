
import math
from heapq import *

# O(KlogN) solution

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pq = []
        for p in points:
            pq.append([self.getDistance(p), p])
        # O(N) time complexity to construct the binary heap
        heapify(pq)

        ans = []
        for i in xrange(K):
            d, p = heappop(pq)
            ans.append(p)

        return ans

    def getDistance(self, p1):
        return math.sqrt(abs(p1[0]) * abs(p1[0]) + abs(p1[1]) * abs(p1[1]))



print Solution().kClosest(points = [[3,3],[5,-1],[-2,4],[4,2],[2,0]], K = 3)
