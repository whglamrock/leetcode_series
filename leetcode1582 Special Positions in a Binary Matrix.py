from collections import defaultdict
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowToOneCount, colToOneCount = defaultdict(int), defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rowToOneCount[i] += 1
                    colToOneCount[j] += 1

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowToOneCount[i] == 1 and colToOneCount[j] == 1:
                    ans += 1

        return ans
