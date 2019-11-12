
from collections import Counter

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        same, countA, countB = Counter(), Counter(A), Counter(B)

        for i in xrange(n):
            if A[i] == B[i]:
                same[A[i]] += 1

        for i in xrange(1, 7):
            # this means on each position, we have at least one i
            if countA[i] + countB[i] - same[i] == len(A):
                return min(countA[i], countB[i]) - same[i]

        return -1



print Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
print Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4])
