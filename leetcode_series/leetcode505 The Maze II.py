
# the non priorityQueue solution will get TLE...lol. Fking stupid leetcode
# However, if we do not use heapq but a dictionary (key is position tuple, value is
#   shortest distance) to be memo, then it won't really help reduce the running time because in
#   worst case (when the distance )

from heapq import *
class Solution(object):
    def shortestDistance(self, maze, start, destination):

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = []
        start = tuple(start)
        destination = tuple(destination)
        pq.append((0, start))
        heapify(pq)
        visited = set()
        res = None

        def go(pos, dir, dist):
            row, col = pos
            x, y = dir
            while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                row += x
                col += y
                dist += 1
            row -= x
            col -= y
            dist -= 1
            if maze[row][col] == 0:
                return dist, (row, col)

        while pq:
            dist, pos = heappop(pq)
            # for a same position, the dist would always be current smallest
            #   because of the heap
            if pos in visited:
                continue
            visited.add(pos)
            if pos == destination:
                res = min(res, dist) if res else dist
            for dir in dirs:
                newdist, newpos = go(pos, dir, dist)
                heappush(pq, (newdist, newpos))

        return res if res else -1