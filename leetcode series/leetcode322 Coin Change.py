# BFS solution, not DP. much faster than DP.
class Solution(object):
    def coinChange(self, coins, amount):

        if amount == 0:
            return 0

        value1 = [0]
        value2 = []
        nc = 0
        visited = [False]*(amount+1)    # or we can build a dict to store all visited values
        #visited[0] = True    # this line actually doesn't affect the operation

        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:   # newval < amount and this newval is not visited
                        visited[newval] = True
                        value2.append(newval)   # value2 records the newly visited values;
                        # in our case, based on value1 == [1,2,5], the next round values can be:
                        # [2,3,6, 3,4,7, 6,7,10], but 1,2,5 have been visited, so they become:
                        # [3,6, 3,4,7, 6,7,10]. Then every distinct number will only be visited once,
                        # so they become [3,6, 4,7, 10], which is the final value2 after this while loop.
            value1, value2 = value2, []

        return -1


Sol = Solution()
coins = [1,2,5]
amount = 11
print Sol.coinChange(coins, amount)


'''
# my original solution with best time complexity got TLE. FUCK.
class Solution(object):
    def coinChange(self, coins, amount):

        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1

        already = {}
        dp = [-1] * (amount+1)
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
                already[coin] = 1

        for i in xrange(1, amount+1):
            for coin in coins:
                if i-coin in already:
                    if dp[i] == -1:
                        dp[i] = dp[i-coin]+1
                    else:
                        dp[i] = min(dp[i], dp[i-coin]+1)
                    already[i] = 1

        return dp[-1]
'''