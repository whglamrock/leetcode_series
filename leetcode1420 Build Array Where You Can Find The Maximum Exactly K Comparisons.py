from functools import lru_cache

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        numOfWays = 0
        for i in range(1, m + 1):
            numOfWays += self.dfs(n - 1, m, k - 1, i)
        return numOfWays % (10 ** 9 + 7)

    @lru_cache(None)
    def dfs(self, n: int, m: int, k: int, currMax: int) -> int:
        mod = 10 ** 9 + 7
        if n == 0:
            if k == 0:
                return 1
            else:
                return 0
        # all numbers (including this one) afterwards need to <= currMax
        if k == 0:
            return (currMax * self.dfs(n - 1, m, 0, currMax)) % mod
        else:
            numOfWays = (currMax * self.dfs(n - 1, m, k, currMax)) % mod
            for i in range(currMax + 1, m + 1):
                numOfWays += self.dfs(n - 1, m, k - 1, i)
                numOfWays %= mod
            return numOfWays
