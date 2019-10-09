
# remember this "modify original matrix" trick, to avoid index out of range

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:
                # note that the variable "row" is not a deep copy
                for row in matrix:
                    ans.append(row.pop())
            if matrix:
                lastRow = matrix.pop()
                ans += lastRow[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))

        return ans



print Solution().spiralOrder(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])

print Solution().spiralOrder(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]])
