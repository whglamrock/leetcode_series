
class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


# think through the idea: we only need to check whether the two adjacent intervals overlap

class Solution(object):
    def canAttendMeetings(self, intervals):

        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)

        for i in xrange(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True



Sol = Solution()
interval1 = Interval(10,30)
interval2 = Interval(15,55)
print Sol.canAttendMeetings([interval1,interval2])
