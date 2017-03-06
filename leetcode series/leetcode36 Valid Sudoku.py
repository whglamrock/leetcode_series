class Solution(object):
    def isValidSudoku(self, board):

        for i in range(9):
            counter1 = 0
            counter2 = 0
            counter3 = 0
            counter4 = 0
            counter5 = 0
            counter6 = 0
            counter7 = 0
            counter8 = 0
            counter9 = 0
            for j in range(9):
                if board[i][j] == '1':
                    counter1 += 1
                    if counter1 > 1:
                        return False
                elif board[i][j] == '2':
                    counter2 += 1
                    if counter2 > 1:
                        return False
                elif board[i][j] == '3':
                    counter3 += 1
                    if counter3 > 1:
                        return False
                elif board[i][j] == '4':
                    counter4 += 1
                    if counter4 > 1:
                        return False
                elif board[i][j] == '5':
                    counter5 += 1
                    if counter5 > 1:
                        return False
                elif board[i][j] == '6':
                    counter6 += 1
                    if counter6 > 1:
                        return False
                elif board[i][j] == '7':
                    counter7 += 1
                    if counter7 > 1:
                        return False
                elif board[i][j] == '8':
                    counter8 += 1
                    if counter8 > 1:
                        return False
                elif board[i][j] == '9':
                    counter9 += 1
                    if counter9 > 1:
                        return False

        for i in range(9):
            counter1 = 0
            counter2 = 0
            counter3 = 0
            counter4 = 0
            counter5 = 0
            counter6 = 0
            counter7 = 0
            counter8 = 0
            counter9 = 0
            for j in range(9):
                if board[j][i] == '1':
                    counter1 += 1
                    if counter1 > 1:
                        return False
                elif board[j][i] == '2':
                    counter2 += 1
                    if counter2 > 1:
                        return False
                elif board[j][i] == '3':
                    counter3 += 1
                    if counter3 > 1:
                        return False
                elif board[j][i] == '4':
                    counter4 += 1
                    if counter4 > 1:
                        return False
                elif board[j][i] == '5':
                    counter5 += 1
                    if counter5 > 1:
                        return False
                elif board[j][i] == '6':
                    counter6 += 1
                    if counter6 > 1:
                        return False
                elif board[j][i] == '7':
                    counter7 += 1
                    if counter7 > 1:
                        return False
                elif board[j][i] == '8':
                    counter8 += 1
                    if counter8 > 1:
                        return False
                elif board[j][i] == '9':
                    counter9 += 1
                    if counter9 > 1:
                        return False

        for i in range(3):
            for j in range(3):
                counter1 = 0
                counter2 = 0
                counter3 = 0
                counter4 = 0
                counter5 = 0
                counter6 = 0
                counter7 = 0
                counter8 = 0
                counter9 = 0
                for k in range(i*3, i*3+3):
                    for l in range(j*3, j*3+3):
                        if board[k][l] == '1':
                            counter1 += 1
                        elif board[k][l] == '2':
                            counter2 += 1
                        elif board[k][l] == '3':
                            counter3 += 1
                        elif board[k][l] == '4':
                            counter4 += 1
                        elif board[k][l] == '5':
                            counter5 += 1
                        elif board[k][l] == '6':
                            counter6 += 1
                        elif board[k][l] == '7':
                            counter7 += 1
                        elif board[k][l] == '8':
                            counter8 += 1
                        elif board[k][l] == '9':
                            counter9 += 1
                    if counter1>1 or counter2>1 or counter3>1 or counter4>1 or counter5>1 or counter6>1 or counter7>1 or counter8>1 or counter9>1:
                        return False

        return True




