
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        coins = sorted(set(coins))

        # dp[i][j] means number of combinations to reach amount j with i coins;
            # this definition will save us the duplicate combination headache (e.g., 1, 1, 2; 1, 2, 1; 2, 1, 1)
        dp = [[0 for j in xrange(amount + 1)] for i in xrange(len(coins) + 1)]
        # we always have one way to reach amount 0
        for i in xrange(len(coins) + 1):
            dp[i][0] = 1

        for i in xrange(1, len(coins) + 1):
            for j in xrange(1, amount + 1):
                # 1) we can completely just not use coins[i - 1]
                dp[i][j] = dp[i - 1][j]
                # 2) we must use coins[i - 1], then j - coins[i - 1] must >= 0
                    # not using dp[i - 1][j - coins[i - 1]] because we can use unlimited number of coins[i - 1]
                if j - coins[i - 1] >= 0:
                    # if we use dp[i - 1][j - coins[i - 1]], consider coins = [1, 2, 5] & amount == 5:
                        # because dp[0] = [1, 0, 0, 0, 0, 0], when we need to calculate dp[1][4]
                        # the dp[1 - 1][4 - 1] = 0 we will get wrong result for dp[1][4]
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[-1][-1]



print Solution().change(5, [1, 2, 5])



'''
# DFS + memoization solution that will get TLE in stupid leetcode OJ but will work in real interview

class Solution(object):
    def change(self, amount, coins):
        if not coins:
            return 0 if amount else 1
        if not amount:
            return 1

        coins = sorted(set(coins))
        return self.dfs(amount, 0, coins, {})

    def dfs(self, amount, i, coins, memo):
        if amount == 0:
            return 1

        if (i, amount) in memo:
            return memo[(i, amount)]

        res = 0
        for j in xrange(i, len(coins)):
            if amount >= coins[j]:
                res += self.dfs(amount - coins[j], j, coins, memo)

        memo[(i, amount)] = res
        return res
'''