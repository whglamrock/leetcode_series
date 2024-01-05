from heapq import *
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        i = 0
        n = len(events)
        numOfEvents = 0
        day = 1

        while day <= 100000:
            if i >= n and not pq:
                break

            # pop out the closed events
            while pq and pq[0] < day:
                heappop(pq)

            # add all open events
            while i < n and events[i][0] <= day:
                heappush(pq, events[i][1])
                i += 1

            # attend one event at a time
            if pq:
                heappop(pq)
                numOfEvents += 1
                day += 1
            # if we popped out all closed events and added all open events
            # the pq is still empty we need to fast forward the day
            else:
                if i < n:
                    day = events[i][0]
                else:
                    day += 1

        return numOfEvents


print(Solution().maxEvents([[1, 2], [2, 3], [3, 4]]))
print(Solution().maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))
print(Solution().maxEvents([[1, 5], [2, 2], [2, 3], [3, 5], [4, 5]]))
print(Solution().maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
print(Solution().maxEvents([[1, 2], [1, 2], [1, 6], [1, 2], [1, 2]]))
print(Solution().maxEvents([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
