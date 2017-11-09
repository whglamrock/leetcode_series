
# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


# the key is to transfer the orginal question into: find the longest non-overlapping
# list of intervals

class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        intervals.sort(key = lambda x: x.end)
        ans = []
        for i in xrange(len(intervals)):
            s, e = intervals[i].start, intervals[i].end
            if not ans:
                ans.append([s, e])
                continue
            if s >= ans[-1][-1]:
                ans.append([s, e])

        return len(intervals) - len(ans)