
from heapq import *

# two pointers: one pointer iterate through all the x coordinates; another iterate through the buildings
    # to push into live pq or pop.
# then naturally the second index would be used with a while loop

# thw following solution is O(NlogN) where N = len(buildings)

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        positions = set()
        for l, r, h in buildings:
            positions.add(l)
            positions.add(r)
        positions = sorted(positions)

        live = []
        heapify(live)

        sky = [[-1, 0]]  # the first used as a "dummy head"
        i, n = 0, len(buildings)

        for pos in positions:
            while i < n and buildings[i][0] <= pos:
                # we need the right edge not left one because we will
                # need it to compare with pos to pop out the dead ones
                heappush(live, [-buildings[i][2], buildings[i][1]])
                i += 1
            # we only care about the tallest building
            while live and live[0][1] <= pos:
                heappop(live)
            # get the current height and add it to live
            h = -live[0][0] if live else 0
            if sky[-1][1] != h:
                sky.append([pos, h])

        return sky[1:]



buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12,], [15, 20, 10,], [19, 24, 8]]
print Solution().getSkyline(buildings)
