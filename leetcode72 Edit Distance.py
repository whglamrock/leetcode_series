
# the key is to find the optimal substructure of dp
# idea from: https://discuss.leetcode.com/topic/20922/java-dp-solution-o-nm

class Solution(object):
    def minDistance(self, word1, word2):

        m, n = len(word1), len(word2)
        # in the dp table, dp[i][j] represents min steps
        #   to match word1[:i] with word2[:j]
        dp = [[2147483647 for j in xrange(n + 1)] for i in xrange(m + 1)]

        for i in xrange(m + 1):
            dp[i][0] = i
        for j in xrange(n + 1):
            dp[0][j] = j

        # the analysis is top-down, but to avoid recursion, we use bottom-up approach
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # replace the char of word1[i - 1] with word2[j - 1]
                    a = dp[i - 1][j - 1]
                    # delete a char at word1[i - 1], let word1[:i] to match word2[:j + 1]
                    b = dp[i - 1][j]
                    # let the original word1[:i + 1] to match word2[:j], and
                        # insert a new char to match word2[j]
                    c = dp[i][j - 1]
                    dp[i][j] = min(a, b, c)
                    dp[i][j] += 1

        return dp[-1][-1]



word1 = 'afsag'
word2 = 'rthates'
Sol = Solution()
print Sol.minDistance(word1, word2)
