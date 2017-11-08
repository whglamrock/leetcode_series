
# Definition for a point.

class Point(object):
    def __init__(self, a=0, b=0):

        self.x = a
        self.y = b


# For same points, we only need to particularly keep a variable 'same', instead of troublesomely
# inserting a slope key 'ANY' in dic.

class Solution(object):
    def maxPoints(self, points):

        m = 0
        for i in xrange(len(points)):
            same = 0
            dic = {'INF': 1}    # for the last point, the dic will stay the default value.
            for j in xrange(i + 1, len(points)):
                jx, jy = points[j].x, points[j].y
                if jx == points[i].x and jy == points[i].y:
                    same += 1
                    continue
                if jx == points[i].x:
                    slope = 'INF'
                else:
                    slope = float(points[i].y - jy) / float(points[i].x - jx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)  # dic.values() retrieve all values in dictionary

        return m