from collections import defaultdict

class GridIllumination:
    def checkIllumination(self, N, lamps, queries):

        # lamps store the location of lamps
        # queries represent the cells that will be checked

        position = set()
        row = defaultdict(int)
        col = defaultdict(int)
        dia = defaultdict(int)
        reversedia = defaultdict(int)

        for lamp in lamps:
            x, y = lamp
            position.add((x, y))
            row[x] += 1
            col[y] += 1
            dia[x - y] += 1
            reversedia[x + y] += 1

        def islight(i, dic):
            # means this row/col/diagonal line was light initially
            if i in dic:
                if dic[i] > 0:  # this line is still light
                    return True
            return False

        ans = []
        for query in queries:
            x, y = query
            xs, ys = [x - 1, x, x + 1], [y - 1, y, y + 1]

            # turn off light:
            for i in xs:
                if 0 < i <= N:
                    for j in ys:
                        if 0 < j <= N and (i, j) in position:
                            row[i] -= 1
                            col[j] -= 1
                            dia[i - j] -= 1
                            reversedia[i + j] -= 1

            lightordark = islight(x, row) + islight(y, col) + islight(x - y, dia) \
                          + islight(x + y, reversedia)
            if lightordark:
                ans.append('LIGHT')
            # if all of the islight judgements return False
            else:
                ans.append('DARK')

            # turn on the light:
            for i in xs:
                if 0 < i <= N:
                    for j in ys:
                        if 0 < j <= N and (i, j) in position:
                            row[i] += 1
                            col[j] += 1
                            dia[i - j] += 1
                            reversedia[i + j] += 1

        return ans


Sol = GridIllumination()
lamps = [[1, 6], [5, 6], [7, 3], [3, 2]]
queries = [[4, 4], [6, 6], [8, 1], [3, 2], [2, 3]]
print Sol.checkIllumination(8, lamps, queries)
