
# recursive DFS. No need to do iterative
# In worst case, the time complexity is still exponential (but running time is much better
    # since we de-dupe a lot of invalid cases).
    # We can add a count global variable to see how many times the dfs function is invoked.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, 0, word):
                    return True

        return False

    def dfs(self, board, i, j, k, word):
        if k == len(word):
            return True
        # out of range
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        if board[i][j] != word[k]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'
        if self.dfs(board, i - 1, j, k + 1, word):
            return True
        if self.dfs(board, i + 1, j, k + 1, word):
            return True
        if self.dfs(board, i, j - 1, k + 1, word):
            return True
        if self.dfs(board, i, j + 1, k + 1, word):
            return True

        board[i][j] = tmp
        return False



print Solution().exist(
    [['A', 'B', 'C', 'E'],
     ['S', 'F', 'C', 'S'],
     ['A', 'D', 'E', 'E']],
    "SEE")

