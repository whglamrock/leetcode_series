from typing import List


# Intuition: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/solutions/876845/java-c-python-easy-and-concise-with-prove/
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ans[i][j]
                colSum[j] -= ans[i][j]

        return ans
