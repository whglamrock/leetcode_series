
from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in xrange(9):
            numCount = {}
            for num in xrange(1, 10):
                count = board[i].count(str(num))
                numCount[num] = count
            if numCount and max(numCount.values()) > 1:
                return False

        for j in xrange(9):
            numCount = defaultdict(int)
            for i in xrange(9):
                if board[i][j] == '.':
                    continue
                numCount[board[i][j]] += 1
            if numCount and max(numCount.values()) > 1:
                return False

        for x in xrange(3):
            for y in xrange(3):
                numCount = defaultdict(int)
                for i in xrange(3 * x, 3 * x + 3):
                    for j in xrange(3 * y, 3 * y + 3):
                        if board[i][j] == '.':
                            continue
                        numCount[board[i][j]] += 1
                if numCount and max(numCount.values()) > 1:
                    return False

        return True




