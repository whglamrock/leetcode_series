
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True

        intervals.sort()
        for i in xrange(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True



print Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]])
