
from heapq import *

# Definition for an interval.

class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# straightforward PriorityQueue Solution. the pq stores the end times

class Solution(object):
    def minMeetingRooms(self, intervals):

        intervals.sort(key = lambda x: x.start)
        pq = []
        numofrooms = 0

        # pq stores the end time
        for interval in intervals:
            while pq and pq[0] <= interval.start:
                heappop(pq)
            heappush(pq, interval.end)
            numofrooms = max(numofrooms, len(pq))

        return numofrooms



intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
Sol = Solution()
print Sol.minMeetingRooms(intervals)



'''
# see explanation from: https://discuss.leetcode.com/topic/20912/my-python-solution-with-explanation

class Solution(object):
    def minMeetingRooms(self, intervals):

        starts = []
        ends = []

        for interval in intervals:
            s, e = interval.start, interval.end
            starts.append(s)
            ends.append(e)

        starts.sort()
        ends.sort()

        numofroom = 0
        # notice the use of available
        available = 0
        s, e = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if not available:
                    numofroom += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1

        return numofroom
'''
