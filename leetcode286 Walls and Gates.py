from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x in range(m):
            for y in range(n):
                if rooms[x][y] != 0:
                    continue

                # bfs
                todo = {(x, y)}
                distance = 0
                while todo:
                    nextTodo = set()
                    for i, j in todo:
                        rooms[i][j] = min(rooms[i][j], distance)
                        for deltaI, deltaJ in directions:
                            ii, jj = i + deltaI, j + deltaJ
                            if 0 <= ii < m and 0 <= jj < n and rooms[ii][jj] > 0 and rooms[ii][jj] > distance + 1:
                                nextTodo.add((ii, jj))
                    todo = nextTodo
                    distance += 1
