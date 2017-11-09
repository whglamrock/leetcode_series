
# simple DFS & Backtracking with memo

class Solution(object):
    def solveNQueens(self, n):

        res = []

        def DFS(queens, cols, diags, reversediags):

            if n == len(queens):
                res.append(queens)
                return

            # i is the row index
            i = len(queens)
            # j is the column index, which will be added to answer list
            for j in xrange(n):
                if j not in cols and i + j not in diags and i - j not in reversediags:
                    DFS(queens + [j], cols | {j}, diags | {i + j}, reversediags | {i - j})

        DFS([], set(), set(), set())
        ans = []
        for sol in res:
            rows = []
            for i in sol:
                rows.append('.' * i + 'Q' + '.' * (n - i - 1))
            ans.append(rows)

        return ans