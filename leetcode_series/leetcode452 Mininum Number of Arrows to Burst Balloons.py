# Greedy Solution: from left to right, try to shoot as many balloons as possible with one arrow

class Solution(object):
    def findMinArrowShots(self, points):

        if not points: return 0
        points.sort(key = lambda x: x[1])

        count = 0
        # notice how to make an infinite number
        currend = -float('inf')

        for s, e in points:
            if s > currend:
                count += 1
                currend = e

        return count