from functools import lru_cache
from math import ceil

# the magic number 4800 needs a bit thinking process.
# check: https://leetcode.com/problems/soup-servings/solutions/121711/c-java-python-when-n-4800-just-return-1/
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        n = ceil(n / 25.0)
        return self.dfs(n, n)

    @lru_cache(None)
    def dfs(self, volumeOfA: int, volumeOfB: int) -> float:
        if volumeOfA <= 0 and volumeOfB <= 0:
            return 0.5
        if volumeOfA <= 0:
            return 1
        if volumeOfB <= 0:
            return 0
        return 0.25 * (self.dfs(volumeOfA - 4, volumeOfB) + self.dfs(volumeOfA - 3, volumeOfB - 1) + self.dfs(volumeOfA - 2, volumeOfB - 2) + self.dfs(volumeOfA - 1, volumeOfB - 3))


print(Solution().soupServings(50))
print(Solution().soupServings(20))
print(Solution().soupServings(100))
print(Solution().soupServings(1000))
print(Solution().soupServings(4799))
print(Solution().soupServings(4801))

'''
class Solution:
    def soupServings(self, n: int) -> float:
        if n == 0:
            return 0.5
        if n > 4800:
            return 1.0
        return self.dfs(n, n)

    @lru_cache(None)
    def dfs(self, volumeOfA: int, volumeOfB: int) -> float:
        ans = 0
        # 1st operation
        if volumeOfA <= 100:
            ans += 0.25
        else:
            ans += 0.25 * self.dfs(volumeOfA - 100, volumeOfB)
        # 2nd operation
        if volumeOfA <= 75:
            # A & B empty at the same time
            if volumeOfB <= 25:
                ans += 0.25 * 0.5
            # A empty first
            else:
                ans += 0.25
        else:
            if volumeOfB > 25:
                ans += 0.25 * self.dfs(volumeOfA - 75, volumeOfB - 25)
        # 3rd operation
        if volumeOfA <= 50:
            # A & B empty at the same time
            if volumeOfB <= 50:
                ans += 0.25 * 0.5
            # A empty first
            else:
                ans += 0.25
        else:
            if volumeOfB > 50:
                ans += 0.25 * self.dfs(volumeOfA - 50, volumeOfB - 50)
        # 4th operation
        if volumeOfA <= 25:
            # A & B empty at the same time
            if volumeOfB <= 75:
                ans += 0.25 * 0.5
            # A empty first
            else:
                ans += 0.25
        else:
            if volumeOfB > 75:
                ans += 0.25 * self.dfs(volumeOfA - 25, volumeOfB - 75)

        return ans
'''

