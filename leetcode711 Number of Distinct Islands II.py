
class Solution(object):
    def numDistinctIslands2(self, grid):

        m, n = len(grid), len(grid[0])
        res = set()

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    shape = []
                    self.dfs(grid, i, j, shape)
                    normalized_repr = self.normalize(shape)
                    res.add(normalized_repr)

        return len(res)

    def dfs(self, grid, r, c, shape):
        grid[r][c] = 0
        shape.append((r, c))

        m, n = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for v, h in dirs:
            nr, nc = r + v, c + h
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                self.dfs(grid, nr, nc, shape)


    def normalize(self, shape):
        # in total 8 mutations
        rotated_shapes = [[] for i in xrange(8)]
        normalized_representations = []

        for x, y in shape:
            rotated_shapes[0].append((x, y))
            rotated_shapes[1].append((-x, y))
            rotated_shapes[2].append((x, -y))
            rotated_shapes[3].append((-x, -y))
            rotated_shapes[4].append((y, x))
            rotated_shapes[5].append((-y, x))
            rotated_shapes[6].append((y, -x))
            rotated_shapes[7].append((-y, -x))

        # need to sort all nodes within each shape to calculate the relative Manhattan distance
        for rs in rotated_shapes:
            rs.sort()
        for rs in rotated_shapes:
            tmp = []
            for i in xrange(1, len(rs)):
                tmp.append((rs[i][0] - rs[0][0], rs[i][1] - rs[0][1]))
            normalized_representations.append(tmp[:])

        normalized_representations.sort()
        return tuple(normalized_representations[0])



Sol = Solution()
grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
print Sol.numDistinctIslands2(grid)

