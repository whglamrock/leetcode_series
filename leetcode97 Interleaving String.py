
# dp[i][j] means s1[:i] & s2[:j] can interleave to s3[:i + j]

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == None or s2 == None or s3 == None:
            return False
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = True

        # it's important to not forget about pre-dealing with corner case
            # because the O(M * N) for loop starts from 1 for both i & j
        for i in xrange(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                           or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]



print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")