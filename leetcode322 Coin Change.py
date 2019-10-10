
# BFS solution, much faster than DP.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        ans = 0
        curr = [0]
        visited = set()

        while curr:
            next = []
            ans += 1
            for value in curr:
                for coin in coins:
                    newValue = value + coin
                    if newValue == amount:
                        return ans
                    if newValue > amount:
                        continue
                    if newValue not in visited:
                        visited.add(newValue)
                        next.append(newValue)
            curr = next

        return -1



print Solution().coinChange([1, 2, 5], 11)



'''
# O(n * amount) DP solution where n = len(coins). It's still way slower than BFS

class Solution(object):
    def coinChange(self, coins, amount):

        if not amount:
            return 0
        
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        for i in xrange(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                        
        return dp[-1]
'''