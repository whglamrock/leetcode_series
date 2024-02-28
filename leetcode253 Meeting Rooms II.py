from heapq import *
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        times = set()
        for start, end in intervals:
            times.add(start)
            times.add(end)
        times = sorted(times)

        pq = []
        i = 0
        roomsNeeded = 0
        for time in times:
            while pq and pq[0] <= time:
                heappop(pq)
            while i < len(intervals) and intervals[i][0] <= time:
                heappush(pq, intervals[i][1])
                i += 1
            roomsNeeded = max(roomsNeeded, len(pq))

        return roomsNeeded


print(Solution().minMeetingRooms([[13, 15], [1, 13]]))
print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))