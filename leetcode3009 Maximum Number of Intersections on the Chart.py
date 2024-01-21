from heapq import *
from typing import List

# spin all line segments vertical. And use a min heap to do line sweep.
# Be careful about how to build the list for sweep values
class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        intervals = []
        for i in range(len(y) - 1):
            intervals.append([y[i], y[i + 1]])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i][1]:
                intervals[i][0] = intervals[i][0] + 0.1
            else:
                intervals[i] = [intervals[i][1], intervals[i][0] - 0.1]
        if intervals[0][0] > intervals[0][1]:
            intervals[0] = [intervals[0][1], intervals[0][0]]
        intervals.sort()

        horizontalLines = set(y)
        distinctY = sorted(set(y))
        for i in range(len(distinctY) - 1):
            horizontalLines.add((distinctY[i] + distinctY[i + 1]) / 2.0)
        horizontalLines = sorted(horizontalLines)

        ans = 0
        i = 0
        pq = []
        for horizontalLine in horizontalLines:
            # add all open intervals
            while i < len(intervals) and intervals[i][0] <= horizontalLine:
                heappush(pq, intervals[i][1])
                i += 1
            # pop out all expired intervals
            while pq and pq[0] < horizontalLine:
                heappop(pq)
            ans = max(ans, len(pq))

        return ans


print(Solution().maxIntersectionCount([9, 10, 2, 10, 5, 8, 2, 6, 2, 1]))
print(Solution().maxIntersectionCount([1, 2, 1, 2, 1, 3, 2]))
print(Solution().maxIntersectionCount([2, 1, 3, 4, 5]))
