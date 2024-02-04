from collections import defaultdict
from heapq import *
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [i for i in range(n)]
        ongoingMeetings = []
        roomToCount = defaultdict(int)

        for start, end in meetings:
            # pop out all completed meetings
            while ongoingMeetings and ongoingMeetings[0][0] <= start:
                finishedEndTime, finishedRoom = heappop(ongoingMeetings)
                heappush(rooms, finishedRoom)
                roomToCount[finishedRoom] += 1

            # see if there's any available room
            if rooms:
                availableRoom = heappop(rooms)
                heappush(ongoingMeetings, [end, availableRoom])
            # delay the meeting until the soonest finished meeting
            else:
                finishedEndTime, finishedRoom = heappop(ongoingMeetings)
                roomToCount[finishedRoom] += 1
                delay = finishedEndTime - start
                heappush(ongoingMeetings, [end + delay, finishedRoom])

        while ongoingMeetings:
            finishedEndTime, finishedRoom = heappop(ongoingMeetings)
            roomToCount[finishedRoom] += 1

        maxRoomCount = 0
        roomWithMostMeeting = 0
        for room in range(n):
            if room not in roomToCount:
                continue
            if roomToCount[room] > maxRoomCount:
                roomWithMostMeeting = room
                maxRoomCount = roomToCount[room]

        return roomWithMostMeeting


print(Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
