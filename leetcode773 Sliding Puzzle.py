from copy import deepcopy
from typing import List, Tuple

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = 0
        todo = {self.serializeBoard(board)}
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while todo:
            nextTodo = set()
            for boardStr in todo:
                if boardStr == '1,2,3,4,5,0':
                    return moves
                visited.add(boardStr)
                currBoard = self.deserializeBoard(boardStr)
                i, j = self.find0Index(currBoard)
                for deltaI, deltaJ in directions:
                    ii, jj = i + deltaI, j + deltaJ
                    if 0 <= ii < 2 and 0 <= jj < 3:
                        newBoard = deepcopy(currBoard)
                        newBoard[i][j] = newBoard[ii][jj]
                        newBoard[ii][jj] = 0
                        newBoardStr = self.serializeBoard(newBoard)
                        if newBoardStr in visited:
                            continue
                        nextTodo.add(newBoardStr)
            todo = nextTodo
            moves += 1

        return -1

    def find0Index(self, board: List[List[int]]) -> Tuple[int, int]:
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return i, j
        # useless, just to avoid syntax error
        return 0, 0

    def serializeBoard(self, board: List[List[int]]) -> str:
        return ','.join(str(item) for item in board[0]) + ',' + ','.join(str(item) for item in board[1])

    def deserializeBoard(self, boardStr: str) -> List[List[int]]:
        nums = boardStr.split(',')
        board = [[], []]
        for i in range(3):
            board[0].append(int(nums[i]))
        for i in range(3, 6):
            board[1].append(int(nums[i]))
        return board


print(Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
print(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
