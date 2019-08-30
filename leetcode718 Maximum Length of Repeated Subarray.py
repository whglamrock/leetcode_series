
# essentially looking for longest common substring

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        m, n = len(A), len(B)
        # dp[i][j] means longest match ends with A[i - 1] & B[j - 1]
        dp = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        maxLen = 0
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                maxLen = max(maxLen, dp[i][j])

        return maxLen



print Solution().findLength([1,2,3,2,1], [3,2,1,4,7])