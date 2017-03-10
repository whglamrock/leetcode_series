# idea came from: https://discuss.leetcode.com/topic/31015/very-easy-to-understand-one-pass-o-n-solution-with-no-extra-space/2
# pay attention to the initial value settings for the following 4 variables.
# O(N) time, O(1) space.
class Solution(object):
    def maxProfit(self, prices):

        n = len(prices)
        if n < 2:
            return 0

        has1_donothing = -prices[0]
        has1_sell = 0
        has0_donothing = 0
        has0_buy = -prices[0]

        for i in xrange(1, n):  # notice the order of update for four variables. only three are based
            # on the previous loop! the has1_sell is based on the has1_donothing on current day.
            has1_donothing = max(has0_buy, has1_donothing)
            has0_buy = has0_donothing - prices[i]
            has0_donothing = max(has1_sell, has0_donothing)
            has1_sell = prices[i] + has1_donothing

        return max(has1_sell, has0_donothing)   # on last day you either sell or do nothing.


Sol = Solution()
prices = [1,4,5,2,9,16]
print Sol.maxProfit(prices)