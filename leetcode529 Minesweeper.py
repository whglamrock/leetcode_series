
# Remember the treatments towards mine how to to the further BFS.
# Too many conditions and terms we need to care, so remember the work flow

from collections import deque

class Solution(object):
    def updateBoard(self, board, click):

        if not board or not board[0]:
            return board

        m, n = len(board), len(board[0])
        queue = deque()
        queue.append(click)

        while queue:
            row, col = queue.popleft()
            if board[row][col] == 'M':
                # we do not return here but just put 'X' to this mine
                board[row][col] = 'X'

            else:
                count = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0:
                            continue
                        r, c = row + i, col + j
                        if r < 0 or r >= m or c < 0 or c >= n:
                            continue
                        if board[r][c] == 'M' or board[r][c] == 'X':
                            count += 1

                if count:
                    board[row][col] = str(count)
                else:
                    # further BFS
                    board[row][col] = 'B'
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if i == 0 and j == 0:
                                continue
                            r, c = row + i, col + j
                            if r < 0 or r >= m or c < 0 or c >= n:
                                continue
                            if board[r][c] == 'E':
                                queue.append([r, c])
                                board[r][c] = 'B'

        return board