
# the trick would be how to build your dp array

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):

        n = len(nums)
        # dp[i][j] means in ith sum (the sum of all i subarrays), the max subarray sum from 0 to j
        dp = [[0 for j in xrange(n)] for i in xrange(4)]
        accuSum = [0] * n
        # indices[i][j] means in ith sum, the starting index of the ith max subarray from 0 to j
        indices = [[0 for j in xrange(n)] for i in xrange(4)]

        currSum = 0
        for i in xrange(n):
            currSum += nums[i]
            # accuSum[i] sums from 0 to i
            accuSum[i] = currSum

        for i in xrange(1, 4):
            # from k - 1, dp[i][j] starts to matter
            for j in xrange(k - 1, n):
                # tmp is actually the newly emerged sum that could "potentially" be the largest
                tmp = accuSum[j] if j == k - 1 else accuSum[j] - accuSum[j - k] + dp[i - 1][j - k]
                # arbitrarily inherit from previous status first
                if j >= k:  # can be removed actually, because dp[i][k - 2] and indices[i][k - 2] were 0 anyways
                    dp[i][j] = dp[i][j - 1]
                    indices[i][j] = indices[i][j - 1]
                # has to be "tmp > dp[i][j - 1]" instead of ">=" because we need lexicographically smallest index
                if j > 0 and tmp > dp[i][j - 1]:
                    dp[i][j] = tmp
                    indices[i][j] = j - k + 1

        res = [0] * 3
        res[2] = indices[3][-1]
        res[1] = indices[2][res[2] - 1]
        res[0] = indices[1][res[1] - 1]
        return res
