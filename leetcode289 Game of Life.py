from typing import List

# Very boring and senseless question from Google.
# currently dead, next alive: 9
# currently dead, next dead: 10
# currently alive, next dead: 11
# currently alive, next alive: 12
class Solution(object):
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.calculateStatus(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.willBeAlive(board, i, j):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    def calculateStatus(self, board: List[List[int]], i: int, j: int) -> int:
        m, n = len(board), len(board[0])
        count = 0
        if i - 1 >= 0 and j - 1 >= 0 and self.isCurrentlyAlive(board, i - 1, j - 1):
            count += 1
        if i - 1 >= 0 and self.isCurrentlyAlive(board, i - 1, j):
            count += 1
        if i - 1 >= 0 and j + 1 < n and self.isCurrentlyAlive(board, i - 1, j + 1):
            count += 1
        if j - 1 >= 0 and self.isCurrentlyAlive(board, i, j - 1):
            count += 1
        if j + 1 < n and self.isCurrentlyAlive(board, i, j + 1):
            count += 1
        if i + 1 < m and j - 1 >= 0 and self.isCurrentlyAlive(board, i + 1, j - 1):
            count += 1
        if i + 1 < m and self.isCurrentlyAlive(board, i + 1, j):
            count += 1
        if i + 1 < m and j + 1 < n and self.isCurrentlyAlive(board, i + 1, j + 1):
            count += 1

        if board[i][j] == 1:
            # currently alive, next alive
            if count == 2 or count == 3:
                return 11
            # currently alive, next dead
            else:
                return 10
        else:
            # currently dead, next alive
            if count == 3:
                return 9
            # currently dead, next dead
            else:
                return 0

    def isCurrentlyAlive(self, board: List[List[int]], i: int, j: int) -> bool:
        if board[i][j] == 1:
            return True
        return board[i][j] == 11 or board[i][j] == 10

    def willBeAlive(self, board: List[List[int]], i: int, j: int) -> bool:
        return board[i][j] == 9 or board[i][j] == 11


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
Solution().gameOfLife(board)
for line in board:
    print(line)
