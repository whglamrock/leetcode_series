from heapq import *
from typing import List

# 1) It's natural to use priority queue to store the height/right edge. The trickiest idea is how to use
# pq to pop out the "dead" buildings as we scan edges from left to right, while also know the height
# of the tallest buildings in priority queue.
# 2) The most import gotcha is: you don't care about non tallest buildings even if they are dead because
# the skyline is only formed by tallest live buildings. So the it's natural to use height as the key for pq.
# 3) pq also stores the right edges. When popping out the pq, only check if pq[0]'s right edge is "dead" or not
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        verticalLines = set()
        for l, r, h in buildings:
            verticalLines.add(l)
            verticalLines.add(r)
        verticalLines = sorted(verticalLines)

        # to deal with edge case when we wanna add the first skyline point
        sky = [[-1, -1]]
        pq = []
        i = 0
        for verticalLine in verticalLines:
            # add all "live" buildings
            while i < len(buildings) and buildings[i][0] <= verticalLine:
                heappush(pq, [-buildings[i][2], buildings[i][1]])
                i += 1

            # only care about the tallest building. there might be some "dead"
            # buildings with shorter height in pq but it's ok
            while pq and pq[0][1] <= verticalLine:
                heappop(pq)

            tallestAlive = -pq[0][0] if pq else 0
            if sky[-1][1] != tallestAlive:
                sky.append([verticalLine, tallestAlive])

        return sky[1:]


print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12, ], [15, 20, 10, ], [19, 24, 8]]))
