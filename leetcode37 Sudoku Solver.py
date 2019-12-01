
# Backtracking. The time complexity is as high as O(9^N), where N is the number of cells to fill.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    continue
                for num in '123456789':
                    if self.isValid(board, i, j, num):
                        board[i][j] = num
                        if self.backtracking(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def isValid(self, board, i, j, num):
        subBox_i = i / 3
        subBox_j = j / 3
        for x in xrange(9):
            if board[i][x] == num or board[x][j] == num:
                return False
            if board[subBox_i * 3 + x / 3][subBox_j * 3 + x % 3] == num:
                return False
        return True