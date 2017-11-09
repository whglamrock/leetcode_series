
# explanation for the skyline problem: https://briangordon.github.io/2014/08/the-skyline-problem.html
# code from: https://discuss.leetcode.com/topic/26420/14-line-python-code-straightforward-easy-to-understand

from heapq import *

# optimal O(NlogN) solution, where n is the number of elements in set(buildings)

class Solution(object):
    def getSkyline(self, buildings):

        if not buildings:
            return []

        # building the positions set is to construct the scanner
        #   in which each scan stop only occurs once
        positions = set()
        for l, r, h in buildings:
            positions.add(l)
            positions.add(r)
        # sorted function changes the set into a sorted list
        positions = sorted(positions)

        live = []
        i = 0
        n = len(buildings)
        # it could any [x, 0]. the second element has to be 0 because of the following if statement
        sky = [[-1, 0]]  # in this case x = -1

        for pos in positions:
            while i < n and buildings[i][0] <= pos:
                heappush(live, [-buildings[i][2], buildings[i][1]])
                i += 1
            # we won't miss the buildings that have been passed, even if such building is short
            while live and live[0][1] <= pos:
                heappop(live)
            h = -live[0][0] if live else 0
            # according to the rules of "key points"
            if sky[-1][-1] != h:
                # we can't append [h, live[0][1]] here because live[0][1] is the right end of a building
                sky.append([pos, h])

        return sky[1:]



Sol = Solution()
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12,], [15, 20, 10,], [19, 24, 8]]
print Sol.getSkyline(buildings)
