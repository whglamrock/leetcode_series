
# idea came from: https://discuss.leetcode.com/topic/31015/very-easy-to-understand-one-pass-o-n-solution-with-no-extra-space/2
# pay attention to the initial value settings for the following 4 variables.
# O(N) time, O(1) space.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)

        # when setting the initial values, think from when i == 1
        has1_sell = 0
        has1_doNothing = -prices[0]
        has0_buy = -prices[0]
        has0_doNothing = 0

        for i in xrange(1, n):
            prev_has1_sell = has1_sell
            prev_has1_doNothing = has1_doNothing
            prev_has0_buy = has0_buy
            prev_has0_doNothing = has0_doNothing

            # Think about how each variable derives from the previous state.
                # 1) if we have 0 and have to buy at i, we couldn't have sold at i - 1 due to cool down limit;
                    # so has0_buy has to be previous has0_doNothing - prices[i]
                # 2) if we have 0 at i, we either sold at i - 1 or did nothing at i - 1;
                    # so has0_doNothing = max(previous has1_sell, previous has0_doNothing)
                # 3) if we have 1 at i, we either bought at i - 1 or already had it before i - 1;
                    # so has1_doNothing = max(previous has1_doNothing, previous has0_buy)
                # 4) if we have 1 at i and we need to sell, we either (already had 1 at i - 1 did nothing at i - 1)
                    # or (bought at i - 1); so has1_sell = max(previous has1_doNothing + prices[i], previous has0_buy + prices[i])

            has0_buy = prev_has0_doNothing - prices[i]
            has0_doNothing = max(prev_has1_sell, prev_has0_doNothing)
            has1_doNothing = max(prev_has1_doNothing, prev_has0_buy)
            has1_sell = max(prev_has1_doNothing + prices[i], prev_has0_buy + prices[i])

        return max(has0_doNothing, has1_sell)



print Solution().maxProfit([1, 4, 5, 2, 9, 16])