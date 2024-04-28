from collections import deque
from typing import List

# Guaranteed O(m * n) time complexity. Using a queue to do a special kind of DFS to make sure we always hit the cell
# with minimum removals first.
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        queue = deque([[0, 0, 0]])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            numOfRemoval, i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return numOfRemoval
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for deltaI, deltaJ in directions:
                ii, jj = i + deltaI, j + deltaJ
                if ii < 0 or ii >= m or j < 0 or jj >= n or (ii, jj) in visited:
                    continue
                if grid[ii][jj] == 1:
                    queue.append([numOfRemoval + 1, ii, jj])
                else:
                    queue.appendleft([numOfRemoval, ii, jj])

        return -1


'''
# naive BFS solution that's probably not gonna satisfy real interview requirement.
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        indexToMinRemoval = {}
        todo = {(0, 0, 0)}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while todo:
            nextTodo = set()
            for i, j, numOfRemoval in todo:
                if (i, j) in indexToMinRemoval and indexToMinRemoval[(i, j)] < numOfRemoval:
                    continue
                indexToMinRemoval[(i, j)] = numOfRemoval

                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n:
                        continue

                    nextNumRemoval = numOfRemoval
                    if grid[ii][jj] == 1:
                        nextNumRemoval += 1
                    if (ii, jj) not in indexToMinRemoval or indexToMinRemoval[(ii, jj)] > nextNumRemoval:
                        nextTodo.add((ii, jj, nextNumRemoval))
                        indexToMinRemoval[(ii, jj)] = nextNumRemoval

            todo = nextTodo

        return indexToMinRemoval[(m - 1, n - 1)]
'''