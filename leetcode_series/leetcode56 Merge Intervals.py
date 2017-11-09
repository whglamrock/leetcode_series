
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
        ans = []
        lo, hi = intervals[0].start, intervals[0].end

        for i in xrange(1, len(intervals)):
            if intervals[i].start <= hi:
                hi = max(hi, intervals[i].end)
            else:
                ans.append(Interval(lo, hi))
                lo, hi = intervals[i].start, intervals[i].end
        ans.append(Interval(lo, hi))

        return ans



Sol = Solution()
intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
ans = Sol.merge(intervals)
for item in ans:
    print item.start, item.end
