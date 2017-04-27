
# explanation for the skyline problem: https://briangordon.github.io/2014/08/the-skyline-problem.html
# code from: https://discuss.leetcode.com/topic/26420/14-line-python-code-straightforward-easy-to-understand

from heapq import *

# optimal O(NlogN) solution, where n is the number of elements in set(buildings)

class Solution(object):
    def getSkyline(self, buildings):

        if not buildings:
            return []

        # because we only add the x position to positions,
        #   we only one of multiple Lis with the same value
        positions = set()
        for item in buildings:
            positions.add(item[0])
            positions.add(item[1])

        # while the vertical line "scans" the sky, the live stores the current "live" positions:
        #   a building is "live" is the current line crosses the building
        live = []
        # it could any [x, 0]. the second element has to be 0 because of the following if statement
        sky = [[-1, 0]]

        i = 0
        # sorted function changes the set into a sorted list
        for t in sorted(positions):
            # add new buildings that are alive now
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, [-buildings[i][2], buildings[i][1]])
                i += 1
            # discard the buildings that have been passed by the scan line
            while live and live[0][1] <= t:
                heappop(live)
            # if we have live buildings, then h != 0
            h = -live[0][0] if live else 0
            # according to the rules of "key points"
            if sky[-1][-1] != h:
                sky.append([t, h])

        return sky[1:]



Sol = Solution()
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12,], [15, 20, 10,], [19, 24, 8]]
print Sol.getSkyline(buildings)
