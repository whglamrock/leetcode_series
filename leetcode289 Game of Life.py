
# Very boring and senseless question from Google.

# currently dead, next alive: 9
# currently dead, next dead: 10
# currently alive, next dead: 11
# currently alive, next alive: 12

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = self.calculateStatus(board, i, j)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.willBeAlive(board, i, j):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    def calculateStatus(self, board, i, j):
        count = 0
        if self.inRange(board, i - 1, j - 1) and self.isCurrentlyAlive(board, i - 1, j - 1):
            count += 1
        if self.inRange(board, i - 1, j ) and self.isCurrentlyAlive(board, i - 1, j):
            count += 1
        if self.inRange(board, i - 1, j + 1) and self.isCurrentlyAlive(board, i - 1, j + 1):
            count += 1
        if self.inRange(board, i, j - 1) and self.isCurrentlyAlive(board, i, j - 1):
            count += 1
        if self.inRange(board, i, j + 1) and self.isCurrentlyAlive(board, i, j + 1):
            count += 1
        if self.inRange(board, i + 1, j - 1) and self.isCurrentlyAlive(board, i + 1, j - 1):
            count += 1
        if self.inRange(board, i + 1, j) and self.isCurrentlyAlive(board, i + 1, j):
            count += 1
        if self.inRange(board, i + 1, j + 1) and self.isCurrentlyAlive(board, i + 1, j + 1):
            count += 1

        if board[i][j] == 1:
            # currently alive, next alive
            if count / 2 == 1:
                return 12
            # currently alive, next dead
            else:
                return 11
        else:
            # currently dead, next alive
            if count == 3:
                return 9
            # currently dead, next dead
            else:
                return 10

    def isCurrentlyAlive(self, board, i, j):
        if board[i][j] == 1:
            return True
        return board[i][j] == 11 or board[i][j] == 12

    def willBeAlive(self, board, i, j):
        return board[i][j] == 9 or board[i][j] == 12

    def inRange(self, board, i, j):
        return 0 <= i < len(board) and 0<= j < len(board[0])



board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Solution().gameOfLife(board)
for line in board:
    print line