from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        numOfBattleShips = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    self.dfs(board, i, j)
                    numOfBattleShips += 1

        return numOfBattleShips

    def dfs(self, board: List[List[str]], i: int, j: int):
        board[i][j] = '.'

        # going downward in the column
        if i + 1 < len(board) and board[i + 1][j] == 'X':
            while i + 1 < len(board) and board[i + 1][j] == 'X':
                board[i + 1][j] = '.'
                i += 1

        # going rightward in the row
        if j + 1 < len(board[0]) and board[i][j + 1] == 'X':
            while j + 1 < len(board[0]) and board[i][j + 1] == 'X':
                board[i][j + 1] = '.'
                j += 1
