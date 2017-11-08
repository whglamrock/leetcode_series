
# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


# the intervals is sorted and non-overlapping
# The following solution is O(n), and idea is to find the insertion position and do potential merge
#   However, we can use binary search to find the position, but insertion/deepcopy both takes O(n).
#   If the intervals is a linkedlist, then there is no way to do binary search. So we can only do O(n)

class Solution(object):
    def insert(self, intervals, newInterval):

        if not intervals:
            return [newInterval]

        s, e = newInterval.start, newInterval.end
        i = 0
        res = []

        while i < len(intervals):
            # potential overlapping
            if s <= intervals[i].end:
                # the newInterval comes completely before intervals[i], no overlapping
                if e < intervals[i].start:
                    break
                # overlapping found
                s, e = min(s, intervals[i].start), max(e, intervals[i].end)
            else:
                res.append(intervals[i])
            i += 1

        res.append(Interval(s, e))
        res.extend(intervals[i:])

        return res