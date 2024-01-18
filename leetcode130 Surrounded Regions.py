from typing import List, Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    connectedIndexes, anyEdgeCells = self.bfs(board, i, j)
                    if not anyEdgeCells:
                        self.modifyBoard(board, connectedIndexes)

    # find all connected index pairs
    def bfs(self, board: List[List[str]], i: int, j: int) -> Tuple[set, bool]:
        todo = {(i, j)}
        ans = set()
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        anyEdgeCells = False
        while todo:
            nextTodo = set()
            for i, j in todo:
                ans.add((i, j))
                if i == m - 1 or j == n - 1 or i == 0 or j == 0:
                    anyEdgeCells = True
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in ans and board[ii][jj] == 'O':
                        nextTodo.add((ii, jj))
            todo = nextTodo

        return ans, anyEdgeCells

    def modifyBoard(self, board: List[List[str]], indexSet: set):
        for i, j in indexSet:
            board[i][j] = 'X'


board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]]
Solution().solve(board)
for row in board:
    print(row)
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]]
Solution().solve(board)
for row in board:
    print(row)
