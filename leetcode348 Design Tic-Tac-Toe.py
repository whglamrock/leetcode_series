
from collections import defaultdict

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        # for player 1
        self.rowToCount1 = defaultdict(int)
        # for player 2
        self.rowToCount2 = defaultdict(int)

        self.colToCount1 = defaultdict(int)
        self.colToCount2 = defaultdict(int)

        self.diaToCount1 = 0
        self.diaToCount2 = 0

        self.reverseDiaToCount1 = 0
        self.reverseDiaToCount2 = 0

    def move(self, row, col, player):
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
        if player == 1:
            self.rowToCount1[row] += 1
            self.colToCount1[col] += 1
            if row == col:
                self.diaToCount1 += 1
            if row + col == self.n - 1:
                self.reverseDiaToCount1 += 1
        else:
            self.rowToCount2[row] += 1
            self.colToCount2[col] += 1
            if row == col:
                self.diaToCount2 += 1
            if row + col == self.n - 1:
                self.reverseDiaToCount2 += 1

        return self.findWinner(row, col)


    def findWinner(self, row, col):
        if self.rowToCount1[row] == self.n \
                or self.colToCount1[col] == self.n \
                or self.diaToCount1 == self.n \
                or self.reverseDiaToCount1 == self.n:
            return 1

        if self.rowToCount2[row] == self.n \
                or self.colToCount2[col] == self.n \
                or self.diaToCount2 == self.n \
                or self.reverseDiaToCount2 == self.n:
            return 2

        return 0



Sol = TicTacToe(3)
print Sol.move(0,0,1)
print Sol.move(0,2,2)
print Sol.move(2,2,1)
print Sol.move(1,1,2)
print Sol.move(2,0,1)
print Sol.move(1,0,2)
print Sol.move(2,1,1)



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)