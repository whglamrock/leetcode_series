
# O(n) time, O(1) space solution

class Solution(object):
    def maxProfit(self, prices, fee):

        # max profit by having no stack after step i
        no_stock_on_hand = 0
        # max profit by having one stack after step i
        have_one_stock_on_hand = -50005

        for price in prices:
            tmp = no_stock_on_hand
            no_stock_on_hand = max(no_stock_on_hand, have_one_stock_on_hand + price - fee)
            have_one_stock_on_hand = max(have_one_stock_on_hand, tmp - price)

        return no_stock_on_hand



Sol = Solution()
prices = [1, 3, 2, 8, 4, 9]
print Sol.maxProfit(prices, 2)



'''
# O(n) space solution

class Solution(object):
    def maxProfit(self, prices, fee):

        if not prices:
            return 0

        n = len(prices)
        # each array[i] means the max profit you can get by doing such operation at day i
        # remember to construct 4 arrays
        buy = [0] * n
        hold = [0] * n
        sell = [0] * n
        # means you do nothing with empty hand
        skip = [0] * n

        buy[0] = 0 - prices[0]
        # this operation based on the assumption that you've already had a share on hand
        hold[0] = 0 - prices[0]

        # the above two initialization is based on the following optimal sub-structure
        for i in xrange(1, n):
            buy[i] = max(sell[i - 1], skip[i - 1]) - prices[i]
            hold[i] = max(hold[i - 1], buy[i - 1])
            skip[i] = max(skip[i - 1], sell[i - 1])
            sell[i] = max(buy[i - 1], hold[i - 1]) + prices[i] - fee

        return max([0, buy[-1], hold[-1], skip[-1], sell[-1]])
'''