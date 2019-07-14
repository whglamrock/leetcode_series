
import math
from heapq import *

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        q = []
        for point in points:
            d = self.distance(point)
            heappush(q, [-d, point])
            if len(q) > K:
                heappop(q)

        ans = []
        while q:
            negativeDistance, point = heappop(q)
            ans.append(point)

        return ans[::-1]

    def distance(self, point):
        return math.sqrt(abs(point[0]) * abs(point[0]) + abs(point[1]) * abs(point[1]))



print Solution().kClosest(points = [[3,3],[5,-1],[-2,4],[4,2],[2,0]], K = 3)
