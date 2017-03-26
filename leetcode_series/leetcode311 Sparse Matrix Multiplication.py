
# Using enumerate in this question is more convenient

class Solution(object):
    def multiply(self, A, B):

        if A == None or B == None:
            return None

        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            return

        C = [[0 for _ in range(l)] for _ in range(m)]
        # the trick is to use the 'if' statement to rule out 0 conditions, thus to limit the number of loops
        for i, row in enumerate(A):
            for k, eleA in enumerate(row): # fasten the element of A instead of the row in A and column in B
                if eleA:    # for A's element A[i][k], it always multiplies the elements in B[k].
                    for j, eleB in enumerate(B[k]):
                        C[i][j] += eleA * eleB

        return C



# in the following case, the element '3' in A will always time the element in [0,0,1] of B.
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Sol = Solution()
print Sol.multiply(A,B)



