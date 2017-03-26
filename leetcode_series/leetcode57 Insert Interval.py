
# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


# Binary search solution, but not necessarily O(logN), because the we need to copy
# the rest of elements in intervals to ans, which takes O(n) time in worst case

class Solution(object):
    def insert(self, intervals, newInterval):

        if not intervals:
            return [newInterval]

        linsert, rinsert = newInterval.start, newInterval.end
        # find which one of the interval the linsert/rinsert can be inserted into
        lindex, rindex = -1, len(intervals)

        l, r = 0, len(intervals) - 1
        # if there is no interval the linsert can be inserted into, we need to find
        # the interval on the left of it so we won't miss the intervals on its left
        # when we form the ans
        ll = -1
        while l <= r:
            mid = l + (r - l) / 2
            lb, rb = intervals[mid].start, intervals[mid].end
            if lb <= linsert <= rb:
                lindex = mid
                break
            elif linsert < lb:
                r = mid - 1
            else:
                l = mid + 1
                ll = mid

        l, r = max(0, lindex), len(intervals) - 1
        # same reason as the one to create ll
        rr = len(intervals)
        while l <= r:
            mid = l + (r - l) / 2
            lb, rb = intervals[mid].start, intervals[mid].end
            if lb <= rinsert <= rb:
                rindex = mid
                break
            elif rinsert < lb:
                r = mid - 1
                rr = mid
            else:
                l = mid + 1

        ans = []
        if lindex != -1:
            for i in xrange(lindex):
                ans.append(intervals[i])
            newlinsert = intervals[lindex].start
        else:
            newlinsert = linsert
            for i in xrange(ll + 1):
                ans.append(intervals[i])

        if rindex != len(intervals):
            newrinsert = intervals[rindex].end
            ans.append(Interval(newlinsert, newrinsert))
            for i in xrange(rindex + 1, len(intervals)):
                ans.append(intervals[i])
        else:
            newrinsert = rinsert
            ans.append(Interval(newlinsert, newrinsert))
            for i in xrange(rr, len(intervals)):
                ans.append(intervals[i])

        return ans