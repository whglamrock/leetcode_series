class TicTacToe(object):
    def __init__(self, n):

        self.n = n
        self.board = [[0 for i in xrange(n)] for j in xrange(n)]
        self.rows = [[n,n] for i in xrange(n)]
        self.cols = [[n,n] for i in xrange(n)]
        self.dias = [[n,n], [n,n]]

    def move(self, row, col, player):

        if self.board[row][col] == 0:
            self.rows[row][player-1] -= 1
            self.cols[col][player-1] -= 1
            self.board[row][col] = 1
            if row == col:
                self.dias[0][player-1] -= 1
            if row + col == self.n-1:
                self.dias[1][player-1] -= 1

            if self.rows[row][player-1] == 0 or self.cols[col][player-1] == 0 or self.dias[0][player-1] == 0 or self.dias[1][player-1] == 0:
                return player
            else:
                return 0

Sol = TicTacToe(3)
print Sol.move(0,0,1)
print Sol.move(0,2,2)
print Sol.move(2,2,1)
print Sol.move(1,1,2)
print Sol.move(2,0,1)
print Sol.move(1,0,2)
print Sol.move(2,1,1)


# for 'move' function:
"""
Player {player} makes a move at ({row}, {col}).
@param row The row of the board.
@param col The column of the board.
@param player The player, can be either 1 or 2.
@return The current winning condition, can be either:
        0: No one wins.
        1: Player 1 wins.
        2: Player 2 wins.
:type row: int
:type col: int
:type player: int
:rtype: int
"""

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)