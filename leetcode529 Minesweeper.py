from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        # bfs
        todo = {(click[0], click[1])}
        while todo:
            nextTodo = set()
            for i, j in todo:
                if board[i][j] == 'M':
                    board[i][j] = 'X'
                    return board

                numOfMines = 0
                adjacentEmptyCells = []
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if ii < 0 or ii >= m or jj < 0 or jj >= n:
                        continue
                    if board[ii][jj] == 'M':
                        numOfMines += 1
                    elif board[ii][jj] == 'E':
                        adjacentEmptyCells.append((ii, jj))
                if numOfMines == 0:
                    for cell in adjacentEmptyCells:
                        nextTodo.add(cell)
                    board[i][j] = 'B'
                else:
                    board[i][j] = str(numOfMines)

            todo = nextTodo

        return board
