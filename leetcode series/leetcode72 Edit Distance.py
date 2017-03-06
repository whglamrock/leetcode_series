# the key is to find the optimal substructure of dp
# idea from: https://discuss.leetcode.com/topic/20922/java-dp-solution-o-nm

class Solution(object):
    def minDistance(self, word1, word2):

        m, n = len(word1), len(word2)
        # in the dp table, dp[i + 1][j + 1] represents min steps
        #   to match word1[:i + 1] with word2[:j + 1]
        dp = [[2147483647 for j in xrange(n + 1)] for i in xrange(m + 1)]

        for i in xrange(m + 1):
            dp[i][0] = i
        for j in xrange(n + 1):
            dp[0][j] = j

        # the analysis is top-down, but to avoid recursion, we use bottom-up approach
        for i in xrange(m):
            for j in xrange(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # replace the char of word1[i] with word2[j]
                    a = dp[i][j]
                    # delete a char at word1[i], let word1[:i] to match word2[:j + 1]
                    b = dp[i][j + 1]
                    # let the original word1[:i + 1] to match word2[:j], and
                    #   insert a new char to match word2[j]
                    c = dp[i + 1][j]
                    dp[i + 1][j + 1] = min(a, b, c)
                    dp[i + 1][j + 1] += 1

        return dp[-1][-1]



word1 = 'afsag'
word2 = 'rthates'
Sol = Solution()
print Sol.minDistance(word1, word2)
