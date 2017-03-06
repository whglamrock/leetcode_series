# iterative O(n^2) solution
class Solution(object):
    def solve(self, board):

        if len(board) == 0 or len(board[0]) == 0:
            return

        queue = []
        for i in xrange(len(board)):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][-1] == 'O':
                queue.append((i,len(board[0])-1))
        for j in xrange(1, len(board[0])-1):
            if board[0][j] == 'O':
                queue.append((0,j))
            if board[-1][j] == 'O':
                queue.append((len(board)-1,j))

        while queue:
            i, j = queue.pop()
            board[i][j] = 'D'
            if i > 0 and board[i-1][j] == 'O':
                queue.append((i-1, j))
            if j > 0 and board[i][j-1] == 'O':
                queue.append((i, j-1))
            if i < len(board)-1 and board[i+1][j] == 'O':
                queue.append((i+1, j))
            if j < len(board[0])-1 and board[i][j+1] == 'O':
                queue.append((i, j+1))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'


Sol = Solution()
board = [["O"]]
print Sol.solve(board)
