
# explanation for the skyline problem: https://briangordon.github.io/2014/08/the-skyline-problem.html
# code from: https://discuss.leetcode.com/topic/26420/14-line-python-code-straightforward-easy-to-understand

import heapq
class Solution(object):
    def getSkyline(self, buildings):

        sky = [[-1, 0]]
        def addsky(pos, hi):
            if sky[-1][-1] != hi:
                sky.append([pos, hi])

        position = set(b[0] for b in buildings) | set(b[1] for b in buildings)
        i = 0
        live = []

        for t in sorted(position):
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, [-buildings[i][2], buildings[i][1]])
                i += 1

            while live and live[0][1] <= t:
                heapq.heappop(live)

            h = -live[0][0] if live else 0
            addsky(t, h)

        return sky[1:]



Sol = Solution()
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12,], [15, 20, 10,], [19, 24, 8]]
print Sol.getSkyline(buildings)
