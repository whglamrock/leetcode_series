# Very boring and senseless question from Google.
class Solution(object):
    def gameOfLife(self, board):

        def check(i,j):
            m,n = len(board), len(board[0])
            count = 0
            if i-1 >= 0 and j-1 >= 0:
                count += board[i-1][j-1][0]
            if i-1 >= 0:
                count += board[i-1][j][0]
            if i-1 >= 0 and j+1 < n:
                count += board[i-1][j+1][0]
            if j-1 >= 0:
                count += board[i][j-1][0]
            if j+1 < n:
                count += board[i][j+1][0]
            if i+1 < m and j-1 >= 0:
                count += board[i+1][j-1][0]
            if i+1 < m:
                count += board[i+1][j][0]
            if i+1 < m and j+1 < n:
                count += board[i+1][j+1][0]

            if board[i][j][0] == 1:
                if count < 2 or count > 3:
                    return 0
                else:
                    return 1
            else:
                if count == 3:
                    return 1
                else:
                    return 0

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = [board[i][j]]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j].append(check(i,j))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = board[i][j][1]

        #return board    # the question asks to return nothing but modify in-place.