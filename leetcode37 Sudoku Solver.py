from typing import List

# Backtracking. The time complexity is as high as O(9^N), where N is the number of cells to fill.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
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

    def isValid(self, board: List[List[str]], i: int, j: int, num: str) -> bool:
        subBoxI = i // 3
        subBoxJ = j // 3
        for x in range(9):
            if board[i][x] == num or board[x][j] == num:
                return False
            if board[subBoxI * 3 + x // 3][subBoxJ * 3 + x % 3] == num:
                return False
        return True
