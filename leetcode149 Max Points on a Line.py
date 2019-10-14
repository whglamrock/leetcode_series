
from collections import defaultdict
from numpy import float128

# use y = k * x + b to identify the points. O(N^2) solution. leetcode corner case is really fucking stupid.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # To deal with duplicate points
        pointCount = defaultdict(int)
        for point in points:
            pointCount[(point[0], point[1])] += 1

        lineToPoints = defaultdict(set)
        for point1 in pointCount.keys():
            for point2 in pointCount.keys():
                if point1 == point2:
                    continue
                k, b = self.calculateParameters(point1, point2)
                lineToPoints[(k, b)].add(point1)
                lineToPoints[(k, b)].add(point2)

        # print lineToPoints
        lineToNumOfPoints = defaultdict(int)
        for k, b in lineToPoints:
            for point in lineToPoints[(k, b)]:
                lineToNumOfPoints[(k, b)] += pointCount[point]

        # need to consider corner case where all points are duplicate
        return max(lineToNumOfPoints.values()) if lineToNumOfPoints else max(pointCount.values())

    def calculateParameters(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x1 == x2:
            k = 'inf'
        else:
            k = float128(y2 - y1) / float128(x2 - x1)
        # when slope is infinite just use x1 to identify this line
        b = y1 - k * x1 if k != 'inf' else x1
        return k, b



print Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
# this leetcode test case is really stupid!
print Solution().maxPoints([[0, 0], [94911151, 94911150], [94911152, 94911151]])
