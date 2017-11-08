
# recursive solution. Sometimes it's hard to find iterative solution for this dfs.

class Solution(object):
    def exist(self, board, word):

        if not word or not board or not board[0]:
            return False

        self.board = board
        m, n = len(board), len(board[0])

        def dfs(i, j, word, k):

            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:  # out of range
                return False
            if self.board[i][j] != word[k]:
                return False

            tmp = self.board[i][j]
            self.board[i][j] = 0    # make the element a number, avoid visit again
            res = dfs(i - 1, j, word, k + 1) or dfs(i + 1, j, word, k + 1) or \
                  dfs(i, j - 1, word, k + 1) or dfs(i, j + 1, word, k + 1)
            self.board[i][j] = tmp

            return res

        for i in xrange(m):
            for j in xrange(n):
                if dfs(i, j, word, 0):
                    return True
        return False



board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
word = "SEE"
Sol = Solution()
print Sol.exist(board, word)

