# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# O(NlogN) solution by sorting.
class Solution(object):
    def merge(self, intervals):

        intervals.sort(key = lambda x: (x.start, x.end))
        ans = []
        curs, cure = None, None  # the start and end of currently merged range
        for i in xrange(len(intervals)):
            if i == 0:
                curs, cure = intervals[i].start, intervals[i].end
            else:
                if intervals[i].start <= cure:
                    cure = max(cure, intervals[i].end)
                else:
                    ans.append([curs, cure])
                    curs, cure = intervals[i].start, intervals[i].end
            #print curs, cure

        if curs != None and cure != None:
            ans.append([curs, cure])

        return ans