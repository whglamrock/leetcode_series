
class Solution(object):
    def wallsAndGates(self, a):
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    stack = [
                        (i + 1, j, 1),
                        (i - 1, j, 1),
                        (i, j + 1, 1),
                        (i, j - 1, 1)
                    ]
                    while stack:
                        ii, jj, dist = stack.pop()
                        if ii < 0 or jj < 0 or ii >= len(a) or jj >= len(a[0]) or a[ii][jj] < dist:
                            continue
                        a[ii][jj] = dist
                        stack.append((ii + 1, jj, dist + 1))
                        stack.append((ii - 1, jj, dist + 1))
                        stack.append((ii, jj + 1, dist + 1))
                        stack.append((ii, jj - 1, dist + 1))

        return a

