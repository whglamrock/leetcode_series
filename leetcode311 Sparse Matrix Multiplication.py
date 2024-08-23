from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n = len(mat1), len(mat2[0])
        ans = [[0 for j in range(n)] for i in range(m)]

        for i, row in enumerate(mat1):
            for j, val1 in enumerate(row):
                for k in range(n):
                    val2 = mat2[j][k]
                    if val1 and val2:
                        ans[i][k] += val1 * val2

        return ans


A = [
    [1, 0, 1],
    [-1, 0, 3]
]
B = [
    [7, 0, 1],
    [0, 0, 0],
    [0, 1, 1]
]
print(Solution().multiply(A, B))
