
'''
the idea is to use the int[] dp to store the length of longest wiggle subsequence that ends with each nums[i]
O(n) solution. The key to it is to notice that dp is a non-decreasing list.
'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums) or len(nums) == 0:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        predif, curdif = 0, 0
        for i in xrange(1, n):
            if curdif != 0:    # predif should record the most recent difference that != 0.
                predif = curdif    # once the first non-zero curdif occurs, the predif will no longer be zero
            curdif = nums[i] - nums[i - 1]
            if (curdif > 0 and predif <= 0) or (curdif < 0 and predif >= 0):
                # the '=' for predif is just for the case when predif hasn't change from zero.
                # that means, the (curdif > 0 and predif == 0) or (curdif < 0 and predif == 0) case occurs only once.
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]

        return dp[n - 1]



