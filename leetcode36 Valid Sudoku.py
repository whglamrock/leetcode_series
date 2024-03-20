from collections import Counter
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numCount = Counter(row)
            if '.' in numCount:
                del numCount['.']
            if numCount and max(numCount.values()) > 1:
                return False

        for j in range(9):
            numSet = set()
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in numSet:
                    return False
                numSet.add(board[i][j])

        indexPairs = [[0, 2], [3, 5], [6, 8]]
        for bottom, top in indexPairs:
            for left, right in indexPairs:
                if self.checkDuplicateInSubBoxes(board, top, bottom, left, right):
                    return False

        return True

    def checkDuplicateInSubBoxes(self, board: List[List[str]], top: int, bottom: int, left: int, right: int) -> bool:
        numSet = set()
        for i in range(bottom, top + 1):
            for j in range(left, right + 1):
                if board[i][j] in numSet:
                    return True
                if board[i][j] != '.':
                    numSet.add(board[i][j])
        return False
