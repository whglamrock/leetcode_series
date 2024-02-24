from typing import List

# For idea, see explanation: https://leetcode.com/problems/find-a-peak-element-ii/solutions/1338377/java-c-detailed-explanation/
# Below is a slightly modified but better to understand version:
# 1) If mat[i][j] < mat[self.findTheMaxRowIndex(mat, j + 1)][j + 1], it means the max of row j is < max of row j + 1
# 2) In this case, we make l = j + 1, so we can "always keep columns[l:r + 1] bigger than its left column and right column"
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l, r = 0, len(mat[0]) - 1
        while l <= r:
            j = (l + r) // 2
            i = self.findTheMaxRowIndex(mat, j)
            if l == r:
                return [i, j]
            if mat[i][j] < mat[self.findTheMaxRowIndex(mat, j + 1)][j + 1]:
                l = j + 1
            else:
                r = j

        return [-1, -1]

    def findTheMaxRowIndex(self, mat: List[List[int]], j: int) -> int:
        maxRowIndex = 0
        for i in range(len(mat)):
            if mat[i][j] > mat[maxRowIndex][j]:
                maxRowIndex = i
        return maxRowIndex
