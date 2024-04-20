from collections import deque
from typing import List

# using deque to preprocess the matrix so we can use popleft(). Otherwise in interview, we may be questioned
# for the O(1) time complexity of list.pop(0) operation
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        modifiedMatrix = deque()
        for row in matrix:
            modifiedMatrix.append(deque(row))
        matrix = modifiedMatrix

        ans = []
        while matrix:
            ans.extend(matrix.popleft())
            if matrix:
                for i in range(len(matrix)):
                    if not matrix[i]:
                        continue
                    ans.append(matrix[i].pop())
            if matrix:
                lastRow = matrix.pop()
                ans.extend(list(lastRow)[::-1])
            if matrix:
                for i in range(len(matrix) - 1, -1, -1):
                    if not matrix[i]:
                        continue
                    ans.append(matrix[i].popleft())

        return ans


print(Solution().spiralOrder(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]))
print(Solution().spiralOrder(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]))
