
# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


# O(NlogN) solution by sorting.

class Solution(object):
    def merge(self, intervals):

        if not intervals:
            return []

        intervals.sort(key = lambda x: x.start)
        currstart = intervals[0].start
        currend = intervals[0].end
        ans = []

        for interval in intervals:
            s, e = interval.start, interval.end
            if s > currend:
                ans.append([currstart, currend])
                currstart, currend = s, e
            else:
                currend = max(currend, e)
        ans.append([currstart, currend])

        res = []
        for item in ans:
            res.append(Interval(item[0], item[1]))
        return res