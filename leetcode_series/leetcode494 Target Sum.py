
# the key is to transfer the problem into subset sum
# O(N * value) classical dp approach, where value is the average value of each element in nums
# see explanation: https://discuss.leetcode.com/topic/76243/java-15-ms-c-3-ms-o-ns-iterative-dp-solution-using-subset-sum-with-explanation

class Solution(object):
    def findTargetSumWays(self, nums, S):

        sumofnums = sum(nums)
        if sumofnums < S or (sumofnums + S) % 2 != 0:
            return 0

        return self.subsetSum(nums, (sumofnums + S) / 2)

    def subsetSum(self, nums, S):

        # using one dimensional dp array and updating all elements in each for loop
        dp = [0 for j in xrange(S + 1)]
        dp[0] = 1

        for num in nums:
            for i in xrange(S, num - 1, -1):
                if dp[i - num] != 0:    # or even save this if statement because "+= 0" still applies
                    dp[i] += dp[i - num]

        return dp[-1]



Sol = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
print Sol.findTargetSumWays(nums, S)
