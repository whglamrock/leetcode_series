# the key is to transfer the problem into subset sum

class Solution(object):
    def findTargetSumWays(self, nums, s):

        sumnums = 0
        for i in xrange(len(nums)):
            sumnums += nums[i]
            nums[i] += nums[i]

        return 0 if sumnums < s else self.subsetSum(nums, s + sumnums)

    # here all elements in nums will be non-negative and we don't need to worry about the symbol
    def subsetSum(self, nums, s):

        n = len(nums)
        # dp[i][j] means the number of ways to get sum i using the first j numbers
        dp = [[0 for j in xrange(n + 1)] for i in xrange(s + 1)]
        dp[0][0] = 1

        for i in xrange(s + 1):
            for j in xrange(1, n + 1):
                # initialize the dp[i][j] with dp[i][j - 1] because we can get sum i by simply
                #   ignore the jth number
                dp[i][j] = dp[i][j - 1]
                # jth number refers nums[j - 1]
                if i - nums[j - 1] >= 0:
                    # we only need to look at the (j - 1)th column here
                    dp[i][j] += dp[i - nums[j - 1]][j - 1]

        return dp[-1][-1]   # i.e., dp[s][n]