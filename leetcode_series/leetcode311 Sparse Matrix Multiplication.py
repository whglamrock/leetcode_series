
# Using enumerate in this question is more convenient
# The key is to consider that row[i] of the result matrix C is the element to element array sum
#   of (row[i][j] of A * row[j] of B).
#   E.g., AB = | 1, 0, 1 |   | 7 0 1 | = | 7 1 2 |
#              |-1, 0, 3 | * | 0 0 0 |   |-7 3 2 |
#                            | 0 1 1 |
#   The 1st row of matrix C is 1 * [7 0 1] + 0 * [0 0 0] + 1 * [0 1 1] = [7 1 2]

class Solution(object):
    def multiply(self, A, B):

        if A == None or B == None or not A or not B or not A[0] or not B[0]:
            return None

        m, n, l = len(A), len(A[0]), len(B[0])
        C = [[0 for i in xrange(l)] for j in xrange(m)]

        for i, row in enumerate(A):
            for j, elementA in enumerate(row):  # focus on a single element of A
                if elementA != 0:
                    # for A's element A[i][k], it always multiplies the elements in B[k].
                    for k, elementB in enumerate(B[j]):
                        C[i][k] += elementA * elementB

        return C



# in the following case, the element '3' in A will always time the element in [0,0,1] of B.

A = [
  [ 1, 0, 1],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 1 ],
  [ 0, 0, 0 ],
  [ 0, 1, 1 ]
]

Sol = Solution()
print Sol.multiply(A,B)



