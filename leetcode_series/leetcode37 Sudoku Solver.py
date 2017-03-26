
# Backtracking. The time complexity is as high as 9 ^ m,
# where m is the number of cells to fill.

class Solution(object):
    def solveSudoku(self, board):

        if not board or not board[0]: return

        def solve(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if isvalid(i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        # at this point, it means we can't find a number to fill this cell,
                        # so it' an invalid board input
                        return False
            # the end of recursion: when all cells are filled properly.
            return True

        def isvalid(row, col, val):
            for i in xrange(9):
                if board[i][col] == val: return False
                if board[row][i] == val: return False
                if board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == val: return False
            return True

        solve(board)