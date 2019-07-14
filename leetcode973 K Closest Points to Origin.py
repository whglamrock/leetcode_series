
import math
from heapq import *

# O(NlogK) solution

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        q = []
        # P.S. building the size K heap actually only takes O(K) time complexity:
            # https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
        for point in points:
            d = self.distance(point)
            heappush(q, [-d, point])
            # in worth case the following operation will be executed N times
            if len(q) > K:
                heappop(q)  # this operation takes O(logK) since we need to heapify again to keep the optimal structure

        ans = []
        while q:
            negativeDistance, point = heappop(q)
            ans.append(point)

        return ans[::-1]

    def distance(self, point):
        return math.sqrt(abs(point[0]) * abs(point[0]) + abs(point[1]) * abs(point[1]))



print Solution().kClosest(points = [[3,3],[5,-1],[-2,4],[4,2],[2,0]], K = 3)
