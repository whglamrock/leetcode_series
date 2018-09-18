
# explanation: https://leetcode.com/problems/my-calendar-ii/discuss/109530/N2-Python-Short-and-Elegant

class MyCalendarTwo(object):

    def __init__(self):

        self.calendar = []
        self.overlap = []

    def book(self, start, end):

        for (i, j) in self.overlap:
            if start < j and end > i:
                return False
        for (i, j) in self.calendar:
            if start < j and end > i:
                self.overlap.append([max(start, i), min(end, j)])
        self.calendar.append([start, end])

        return True