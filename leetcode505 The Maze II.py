
from heapq import *

# Using heapq won't reduce the mathematical time complexity, but can make sure we don't make redundant BFS
# Time complexity should be O(M * N)

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        start, destination = tuple(start), tuple(destination)
        # pq is the min distance pq
        pq = [(0, start)]
        heapify(pq)

        ans = 2147483647
        visited = set()

        while pq:
            distance, position = heappop(pq)
            # because we visited the same position with min distance first, we don't change the ans here
            if position in visited:
                continue
            visited.add(position)

            if position == destination:
                ans = distance
                break

            # we have to do BFS here, not DFS
            for direction in dirs:
                newDist, newPos = self.go(position, maze, direction, distance)
                if newPos not in visited:
                    heappush(pq, (newDist, newPos))

        return ans if ans != 2147483647 else -1

    def go(self, curr, maze, direction, distance):
        i, j = curr
        x, y = direction

        while 0 <= i + x < len(maze) and 0 <= j + y < len(maze[0]) and maze[i + x][j + y] != 1:
            i += x
            j += y
            distance += 1

        return distance, (i, j)