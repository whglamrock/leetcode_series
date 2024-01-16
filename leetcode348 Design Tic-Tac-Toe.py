from collections import defaultdict

class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rowToMarkCount1 = defaultdict(int)
        self.rowToMarkCount2 = defaultdict(int)
        self.colToMarkCount1 = defaultdict(int)
        self.colToMarkCount2 = defaultdict(int)
        self.topLeftToBottomRightMarkCount1 = 0
        self.topLeftToBottomRightMarkCount2 = 0
        self.topRightToBottomLeftMarkCount1 = 0
        self.topRightToBottomLeftMarkCount2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rowToMarkCount1[row] += 1
            if self.rowToMarkCount1[row] == self.n:
                return 1
            self.colToMarkCount1[col] += 1
            if self.colToMarkCount1[col] == self.n:
                return 1
            if row == col:
                self.topLeftToBottomRightMarkCount1 += 1
                if self.topLeftToBottomRightMarkCount1 == self.n:
                    return 1
            if row + col == self.n - 1:
                self.topRightToBottomLeftMarkCount1 += 1
                if self.topRightToBottomLeftMarkCount1 == self.n:
                    return 1
        else:
            self.rowToMarkCount2[row] += 1
            if self.rowToMarkCount2[row] == self.n:
                return 2
            self.colToMarkCount2[col] += 1
            if self.colToMarkCount2[col] == self.n:
                return 2
            if row == col:
                self.topLeftToBottomRightMarkCount2 += 1
                if self.topLeftToBottomRightMarkCount2 == self.n:
                    return 2
            if row + col == self.n - 1:
                self.topRightToBottomLeftMarkCount2 += 1
                if self.topRightToBottomLeftMarkCount2 == self.n:
                    return 2
        return 0


sol = TicTacToe(3)
print(sol.move(0, 0, 1))
print(sol.move(0, 2, 2))
print(sol.move(2, 2, 1))
print(sol.move(1, 1, 2))
print(sol.move(2, 0, 1))
print(sol.move(1, 0, 2))
print(sol.move(2, 1, 1))


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
