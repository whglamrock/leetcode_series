
# the key is to define dp[i][j], and which previous dp[i][j] we should use for each option
# idea from: https://discuss.leetcode.com/topic/20922/java-dp-solution-o-nm

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # dp[i][j] means the min steps for word1[:i] to match word2[:j]
        dp = [[2147483647 for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[0][0] = 0

        # there is no other option for word1 to match with an empty string
        for i in xrange(1, m + 1):
            dp[i][0] = i
        # there is no other option for word2 to match with an empty string
        for j in xrange(1, n + 1):
            dp[0][j] = j

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # compare 3 options
                else:
                    # insert a char in word1 to match the extra word2[j - 1];
                        # so we need the min steps for matching word1[:i] with word2[:j - 1]
                    a = dp[i][j - 1]
                    # delete a char; so we need the min steps for matching
                        # word1[:i - 1] with word2[:j]
                    b = dp[i - 1][j]
                    # replace a char
                    c = dp[i - 1][j - 1]
                    dp[i][j] = min(a, b, c) + 1

        return dp[-1][-1]



word1 = 'afsag'
word2 = 'rthates'
Sol = Solution()
print Sol.minDistance(word1, word2)
