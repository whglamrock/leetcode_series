from heapq import *
from typing import List

# maintain a min heap of size ladders, in which we add all height differences. The idea is we would wanna use
# bricks against the smallest height differences.
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(len(heights) - 1):
            distance = heights[i + 1] - heights[i]
            if distance > 0:
                heappush(pq, distance)
            # ladders alone won't cover all jumps, have to use bricks, then choose
            # the smallest height difference to use the fewest bricks
            if len(pq) > ladders:
                bricks -= heappop(pq)
            if bricks < 0:
                return i

        return len(heights) - 1
