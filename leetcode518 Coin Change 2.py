
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
        # we always have a way to reach amount 0
        for i in xrange(len(coins) + 1):
            dp[i][0] = 1

        for i in xrange(1, len(coins) + 1):
            for j in xrange(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
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