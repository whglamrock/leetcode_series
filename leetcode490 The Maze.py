from typing import List

# O(m * n) BFS solution. Note that we don't check visited until we make a turn. This is to deal with an edge case
# where we would otherwise incorrectly make a turn in a non-near-wall position.
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        leftVisited, rightVisited, upVisited, downVisited = set(), set(), set(), set()
        directionToVisited = {'up': upVisited, 'down': downVisited, 'left': leftVisited, 'right': rightVisited}
        todo = [[start[0], start[1], 'up'], [start[0], start[1], 'down'], [start[0], start[1], 'left'], [start[0], start[1], 'right']]
        m, n = len(maze), len(maze[0])

        while todo:
            nextTodo = []
            for i, j, direction in todo:
                if i == destination[0] and j == destination[1] and self.cantMove(maze, i, j, direction):
                    return True
                if (i, j) in directionToVisited[direction]:
                    continue
                directionToVisited[direction].add((i, j))
                # don't check visited here until making a turn
                if direction == 'up' and (i - 1 >= 0 and maze[i - 1][j] == 0):
                    nextTodo.append([i - 1, j, 'up'])
                elif direction == 'down' and (i + 1 < m and maze[i + 1][j] == 0):
                    nextTodo.append([i + 1, j, 'down'])
                elif direction == 'left' and (j - 1 >= 0 and maze[i][j - 1] == 0):
                    nextTodo.append([i, j - 1, 'left'])
                elif direction == 'right' and (j + 1 < n and maze[i][j + 1] == 0):
                    nextTodo.append([i, j + 1, 'right'])
                # can't keep moving in original direction, see if we can turn
                else:
                    if (i - 1 >= 0 and maze[i - 1][j] == 0) and (i - 1, j) not in upVisited:
                        nextTodo.append([i - 1, j, 'up'])
                    if (i + 1 < m and maze[i + 1][j] == 0) and (i + 1, j) not in downVisited:
                        nextTodo.append([i + 1, j, 'down'])
                    if (j - 1 >= 0 and maze[i][j - 1] == 0) and (i, j - 1) not in leftVisited:
                        nextTodo.append([i, j - 1, 'left'])
                    if (j + 1 < n and maze[i][j + 1] == 0) and (i, j + 1) not in rightVisited:
                        nextTodo.append([i, j + 1, 'right'])

            todo = nextTodo

        return False

    def cantMove(self, maze: List[List[int]], i: int, j: int, direction: str) -> bool:
        if direction == 'up':
            return i - 1 < 0 or maze[i - 1][j] == 1
        if direction == 'down':
            return i + 1 >= len(maze) or maze[i + 1][j] == 1
        if direction == 'left':
            return j - 1 < 0 or maze[i][j - 1] == 1
        if direction == 'right':
            return j + 1 >= len(maze[0]) or maze[i][j + 1] == 1
        return False


print(Solution().hasPath([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0], [1, 2]))
