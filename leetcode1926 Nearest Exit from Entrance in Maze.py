from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m, n = len(maze), len(maze[0])
        todo = [entrance]
        step = 0
        while todo:
            nextTodo = []
            for i, j in todo:
                # fill the cell
                maze[i][j] = '+'
                # at the border
                if [i, j] != entrance and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    return step
                # prefill the cells in the next round to speed up the bfsN
                if i - 1 >= 0 and maze[i - 1][j] == '.':
                    maze[i - 1][j] = '+'
                    nextTodo.append([i - 1, j])
                if i + 1 < m and maze[i + 1][j] == '.':
                    maze[i + 1][j] = '+'
                    nextTodo.append([i + 1, j])
                if j - 1 >= 0 and maze[i][j - 1] == '.':
                    maze[i][j - 1] = '+'
                    nextTodo.append([i, j - 1])
                if j + 1 < n and maze[i][j + 1] == '.':
                    maze[i][j + 1] = '+'
                    nextTodo.append([i, j + 1])
            step += 1
            todo = nextTodo

        return -1


print(Solution().nearestExit(
    [["+", "+", ".", "+"],
     [".", ".", ".", "+"],
     ["+", "+", "+", "."]],
    [0, 1]
))
print(Solution().nearestExit(
    [["+", "+", "+"],
     [".", ".", "."],
     ["+", "+", "+"]],
    [1, 0]
))
print(Solution().nearestExit(
    [[".", "+"]],
    [0, 0]
))
print(Solution().nearestExit(
    [["."]],
    [0, 0]
))
print(Solution().nearestExit(
    [["+", ".", "+", "+", "+", "+", "+"],
     ["+", ".", "+", ".", ".", ".", "+"],
     ["+", ".", "+", ".", "+", ".", "+"],
     ["+", ".", ".", ".", "+", ".", "+"],
     ["+", "+", "+", "+", "+", "+", "."]],
    [0, 1]
))
