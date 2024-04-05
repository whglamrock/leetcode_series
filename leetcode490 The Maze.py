from typing import List

# Below solution is easier to implement (way less code) and less error-prone than using visited set for each direction.
# Also notice that in BFS we don't add the position to the nextTodo unless we can stop.
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        todo = {(start[0], start[1])}

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while todo:
            nextTodo = set()
            for i, j in todo:
                if i == destination[0] and j == destination[1]:
                    return True
                # change it to 2 so we shouldn't stop at this position again
                # but not change it to 1 because we can still move through it
                maze[i][j] = 2
                for deltaI, deltaJ in directions:
                    # remember the below setup for the maze problem (stop until hitting the wall)
                    ii, jj = i + deltaI, j + deltaJ
                    while 0 <= ii < m and 0 <= jj < n and maze[ii][jj] != 1:
                        ii += deltaI
                        jj += deltaJ
                    ii -= deltaI
                    jj -= deltaJ
                    if maze[ii][jj] == 0:
                        nextTodo.add((ii, jj))

            todo = nextTodo

        return False


print(Solution().hasPath([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0], [1, 2]))
