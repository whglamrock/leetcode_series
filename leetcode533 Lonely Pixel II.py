
from collections import defaultdict

class Solution(object):
    def findBlackPixel(self, picture, N):

        rowdic = defaultdict(list)
        rows, cols = defaultdict(int), defaultdict(int)

        for i, row in enumerate(picture):
            rowkey = ''.join(row)
            rowdic[rowkey].append(i)
            for j, char in enumerate(row):
                if char == 'B':
                    rows[i] += 1
                    cols[j] += 1

        ans = 0
        for rowkey in rowdic:
            for j, char in enumerate(rowkey):
                # rule2 and column aspect of rule1
                if char != 'B' or cols[j] != N or len(rowdic[rowkey]) != N:
                    continue
                # anyone row index is okay because these rows are the same
                i = rowdic[rowkey][0]
                # row aspect of rule1
                if rows[i] == N:
                    ans += N

        return ans



picture = [['W', 'B', 'W', 'B', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'B', 'W'],
           ['W', 'W', 'B', 'W', 'B', 'W']]
Sol = Solution()
print Sol.findBlackPixel(picture, 3)

