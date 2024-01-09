from heapq import *
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        roomsNeeded = 0
        intervals.sort()
        pq = []
        for start, end in intervals:
            while pq and pq[0] <= start:
                heappop(pq)
            heappush(pq, end)
            roomsNeeded = max(roomsNeeded, len(pq))

        return roomsNeeded


print(Solution().minMeetingRooms([[13, 15], [1, 13]]))
print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))