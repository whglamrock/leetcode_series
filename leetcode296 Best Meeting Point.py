class Solution(object):
    def minTotalDistance(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = [], []
        m, n = len(grid), len(grid[0])

        # Because we are looping through the whole grid, row & col lists are sorted
        # Each row/col can have multiple people so we use median (not avg) as best meeting point
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        # x, y is the idea meeting point
        x, y = rows[len(rows) // 2], cols[len(cols) // 2]
        ans = 0
        for row in rows:
            ans += abs(row - x)
        for col in cols:
            ans += abs(col - y)

        return ans


print(Solution().minTotalDistance([
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]]))
