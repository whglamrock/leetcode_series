from heapq import *

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

# Idea from merge k sorted list. The difference is, here we need to merge each interval popped out from the priorityQueue.
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        pq = []
        for i, employeeIntervals in enumerate(schedule):
            interval = employeeIntervals[0]
            heappush(pq, [[interval.start, interval.end], i, 0])

        currMergedInternal = []
        ans = []
        while pq:
            interval, i, j = heappop(pq)
            if not currMergedInternal:
                currMergedInternal = interval
            else:
                # intersection
                if interval[0] <= currMergedInternal[1]:
                    currMergedInternal[1] = max(interval[1], currMergedInternal[1])
                # no intersection
                else:
                    ans.append(Interval(currMergedInternal[1], interval[0]))
                    currMergedInternal = interval
            if j + 1 < len(schedule[i]):
                newInterval = schedule[i][j + 1]
                heappush(pq, [[newInterval.start, newInterval.end], i, j + 1])

        return ans
