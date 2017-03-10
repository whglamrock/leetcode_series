# we burst from the last balloon
class Solution(object):
    def maxCoins(self, inums):

        nums = [1] + inums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        # dp[left][right] means the score we get after burst from index left + 1 to index right - 1
            # (0 <= left; left + k <= right < n)
        # k is the length of range, k = 2 initially because the bottom case is we burst every triplet.
        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1, right):
                    # it's nums[left] * nums[i] * nums[right] because we actually look at
                        # that the nums[left], nums[i], nums[right] are adjacent to each other,
                        # where nums[left + 1: i] and nums[i + 1: right] are already burst
                        # and dp[left][i] & dp[i][right] are saved in the previous for loops.
                    # the nums[left], nums[i], nums[right] are triplet that need to be burst in this round
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

        return dp[0][n - 1]