from typing import List

# BFS solution, fastest and easiest to implement in real interview.
# another dp idea that's similar: https://leetcode.com/problems/coin-change/solutions/778548/c-dp-solution-explained-100-time-100-space/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        visited = set()
        todo = [0]
        ans = 0

        # each while loop is a bfs, which adds one more coin
        while todo:
            nextTodo = []
            ans += 1
            for currAmount in todo:
                for coin in coins:
                    newAmount = currAmount + coin
                    if newAmount == amount:
                        return ans
                    if newAmount > amount:
                        continue
                    if newAmount not in visited:
                        visited.add(newAmount)
                        nextTodo.append(newAmount)
            todo = nextTodo

        return -1


print(Solution().coinChange([1, 2, 5], 11))


'''
# O(n * amount) DP solution where n = len(coins). It's still way slower than BFS
# dp[i] is the min amount coins needed to reach money i
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        coins = set(coins)

        for i in range(1, amount + 1):
            for j in range(i):
                if (i - j) in coins and dp[j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
'''