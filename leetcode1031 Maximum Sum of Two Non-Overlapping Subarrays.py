
# such question is usually asked in onsite so whiteboarding helps figuring out the solution

class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):

        # just modify the original array instead of building a new prefixSum array
        for i in xrange(1, len(A)):
            A[i] += A[i - 1]

        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]

        # window  | --- L --- | --- M --- |
            # i is the right edge of M window, so Lmax can be any L block in A[:i - M + 1]
        for i in xrange(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - M - L])
            res = max(res, Lmax + A[i] - A[i - M])

        # window  | --- M --- | --- L --- |
            # i is the right edge of L window, so Mmax can be any M block in A[:i - L + 1]
        for i in xrange(L + M, len(A)):
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Mmax + A[i] - A[i - L])

        return res



print Solution().maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3)