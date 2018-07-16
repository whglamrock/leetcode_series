
# we assume start and destination are not 1

from heapq import *

class Solution(object):
    def shortestDistance(self, maze, start, destination):

        res = None
        visited = set()
        pq = []
        start = tuple(start)
        destination = tuple(destination)
        pq.append((0, start))
        heapify(pq)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def go(pos, direction, dist):
            row, col = pos
            x, y = direction
            while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                row += x
                col += y
                dist += 1
            row -= x
            col -= y
            dist -= 1
            return dist, (row, col)

        while pq:
            # using heapq will reduce the theoretical time complexity, but can make sure we always try out
            #   the shortest path first then filter out the longer solution using visited set
            dist, pos = heappop(pq)
            if pos in visited:
                continue
            visited.add(pos)
            if pos == destination:
                res = min(res, dist) if res else dist
            for direction in dirs:
                newDist, newPos = go(pos, direction, dist)
                # only add meaningful nextPosition
                if newPos not in visited:
                    heappush(pq, (newDist, newPos))

        return res if res else -1