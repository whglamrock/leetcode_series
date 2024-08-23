from collections import defaultdict
from heapq import *
from typing import List


# we cannot add all start & end times from meetings and use a sorted timeline list to loop it through:
# 1) it's very possible we skipped some expired meeting end times (those end times are delayed by some delta). e.g.,
# the timeline could be 17 and we have some meeting that originally ends at 13 but actual end time is 14 (13 + delay of 1),
# but the timeline set doesn't included a point of time == 14 (only 13, 17). In this case there could be some meeting
# already waiting that should have been added to the room released by the meeting ends at 14, but wrongfully added to
# the room that's released by the meeting ends at 17
# 2) to bypass this limitation, you might think of looping through all 10 ** 9 + 7 time values but it will get TLE in
# the stupid leetcode. The easiest way to solve it is just going through the sorted meetings list, not using a timeline set.
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ongoingMeetings = []
        availableRooms = [i for i in range(n)]
        roomToCount = defaultdict(int)

        for start, end in meetings:
            while ongoingMeetings and ongoingMeetings[0][0] <= start:
                finishedEnd, finishedRoom = heappop(ongoingMeetings)
                heappush(availableRooms, finishedRoom)

            if availableRooms:
                room = heappop(availableRooms)
                heappush(ongoingMeetings, [end, room])
            else:
                earliestEnd, room = heappop(ongoingMeetings)
                newEnd = max(earliestEnd, start) + (end - start)
                heappush(ongoingMeetings, [newEnd, room])

            roomToCount[room] += 1

        maxCount = max(roomToCount.values())
        for i in range(n):
            if i in roomToCount and roomToCount[i] == maxCount:
                return i

        return 0


print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
