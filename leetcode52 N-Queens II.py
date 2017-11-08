
class Solution(object):
    def totalNQueens(self, n):

        self.count = 0

        def DFS(i, cols, diags, reversediags):

            if i == n:
                self.count += 1
                return

            # i is the row index
            # j is the column index, which will be added to answer list
            for j in xrange(n):
                if j not in cols and i + j not in diags and i - j not in reversediags:
                    DFS(i + 1, cols | {j}, diags | {i + j}, reversediags | {i - j})

        DFS(0, set(), set(), set())
        return self.count