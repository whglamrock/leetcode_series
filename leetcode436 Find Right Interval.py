
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# O(nlogn) binary search solution

class Solution(object):
    def findRightInterval(self, intervals):

        original = {}
        for i in xrange(len(intervals)):
            original[intervals[i].start] = i
        intervals.sort(key = lambda x: x.start)

        ans = {}
        for i in xrange(len(intervals)):
            l, r = 0, len(intervals) - 1
            while l < r:
                mid = l + (r - l) / 2
                if intervals[mid].start >= intervals[i].end:
                    r = mid
                else:
                    l = mid + 1
            if intervals[l].start >= intervals[i].end and l != i:
                ans[original[intervals[i].start]] = original[intervals[l].start]
            else:
                ans[original[intervals[i].start]] = -1
        #print ans

        res = []
        for i in xrange(len(intervals)):
            res.append(ans[i])

        return res