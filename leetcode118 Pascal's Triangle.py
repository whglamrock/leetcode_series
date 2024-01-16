from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]
        currRow = [1, 1]
        for i in range(2, numRows):
            nextRow = []
            for j in range(i + 1):
                if j == 0:
                    nextRow.append(1)
                elif j == i:
                    nextRow.append(1)
                else:
                    nextRow.append(currRow[j] + currRow[j - 1])
            ans.append(nextRow)
            currRow = nextRow

        return ans


print(Solution().generate(11))
