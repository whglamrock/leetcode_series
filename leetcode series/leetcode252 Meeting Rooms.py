
class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


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



'''
# The original sloppy solution with time complexity o(nlogn)

class Solution(object):
    def canAttendMeetings(self, intervals):

        timing = []
        for item in intervals:
            timing.append([item.start, item.end])
        timing.sort()

        for i in xrange(len(timing) - 1):
            if timing[i+1][0] < timing[i][1]:
                return False

        return True
'''