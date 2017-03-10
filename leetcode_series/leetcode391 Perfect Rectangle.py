from collections import defaultdict

class Solution(object):
    def isRectangleCover(self, rectangles):

        if (not rectangles) or len(rectangles) == 0 or len(rectangles[0]) == 0:
            return False

        left, right, bottom, top = 2147483647, -2147483648, 2147483647, -2147483648
        areasum = 0
        points = defaultdict()

        for rec in rectangles:

            left = min(rec[0], left)
            right = max(rec[2], right)
            bottom = min(rec[1], bottom)
            top = max(rec[3], top)

            areasum += (rec[2] - rec[0]) * (rec[3] - rec[1])
            s1 = (rec[0], rec[1])
            s2 = (rec[0], rec[3])
            s3 = (rec[2], rec[1])
            s4 = (rec[2], rec[3])

            if s1 not in points:
                points[s1] = 1
            else:
                points[s1] += 1
            if s2 not in points:
                points[s2] = 1
            else:
                points[s2] += 1
            if s3 not in points:
                points[s3] = 1
            else:
                points[s3] += 1
            if s4 not in points:
                points[s4] = 1
            else:
                points[s4] += 1

        if (left, bottom) not in points or (left, top) not in points or (right, bottom) not in points or (right, top) not in points:
            return False

        pointset = {(left, bottom), (left, top), (right, bottom), (right, top)}
        # every point either appears twice/four times, or is the corner point of the big rectangle.
        for point in points:
            if points[point] % 2!= 0 and point not in pointset:
                return False

        # if there are two completely overlapping recs:
        return areasum == (right - left) * (top - bottom)