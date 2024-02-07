from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        connectedCells = set()
        for i in range(len(board)):
            connectedCells = connectedCells.union(self.findConnectedCellsInRow(board, i))
        for j in range(len(board[0])):
            connectedCells = connectedCells.union(self.findConnectedCellsInColumn(board, j))

        while connectedCells:
            # crush the candy
            for i, j in connectedCells:
                board[i][j] = 0
            # drop the candies
            for j in range(len(board[0])):
                numOf0sToSkip = 0
                for i in range(len(board) - 1, -1, -1):
                    if board[i][j] == 0:
                        numOf0sToSkip += 1
                    else:
                        board[i + numOf0sToSkip][j] = board[i][j]
                        if numOf0sToSkip != 0:
                            board[i][j] = 0

            # find new connected candies
            connectedCells = set()
            for i in range(len(board)):
                connectedCells = connectedCells.union(self.findConnectedCellsInRow(board, i))
            for j in range(len(board[0])):
                connectedCells = connectedCells.union(self.findConnectedCellsInColumn(board, j))

        return board

    def findConnectedCellsInRow(self, board: List[List[int]], i: int) -> set:
        ans = set()
        numOfConsecutive = 1
        for j in range(1, len(board[0])):
            if board[i][j] != 0 and board[i][j] == board[i][j - 1]:
                numOfConsecutive += 1
            else:
                if numOfConsecutive >= 3:
                    for k in range(j - numOfConsecutive, j):
                        ans.add((i, k))
                numOfConsecutive = 1

        if numOfConsecutive >= 3:
            for k in range(len(board[0]) - numOfConsecutive, len(board[0])):
                ans.add((i, k))

        return ans

    def findConnectedCellsInColumn(self, board: List[List[int]], j: int) -> set:
        ans = set()
        numOfConsecutive = 1
        for i in range(1, len(board)):
            if board[i][j] != 0 and board[i][j] == board[i - 1][j]:
                numOfConsecutive += 1
            else:
                if numOfConsecutive >= 3:
                    for k in range(i - numOfConsecutive, i):
                        ans.add((k, j))
                numOfConsecutive = 1

        if numOfConsecutive >= 3:
            for k in range(len(board) - numOfConsecutive, len(board)):
                ans.add((k, j))

        return ans
