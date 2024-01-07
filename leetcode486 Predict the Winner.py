from functools import lru_cache
from typing import List

# Cached dfs solution: on surface it looks like O(2^N) time due to recursion, but it's actually O(N * N) with cache.
# It == the number of nums' subsequence, which is n + (n - 1) + (n - 2) + ... + 2 + 1 == n * (n + 1) / 2.
class Solution:
    def __init__(self):
        self.nums = []

    def predictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        return self.dfs(0, len(nums) - 1) >= sum(nums) / 2

    # dfs gets the max score any player (1 or 2) can get from nums[l:r + 1]
    @lru_cache(None)
    def dfs(self, l: int, r: int) -> int:
        if l > r:
            return 0

        # 1. Next player (assuming it's 2) needs to choose nums[l + 1], or nums[r] in the next round.
        # 2. self.dfs(l + 2, r) ==> means nums[l + 1] is taken by player 2, so it's removed from player 1's score
        # that he can get from the next + 1 round; same idea for self.dfs(l + 1, r - 1)
        chooseLeft = self.nums[l] + min(self.dfs(l + 2, r), self.dfs(l + 1, r - 1))
        # same idea
        chooseRight = self.nums[r] + min(self.dfs(l + 1, r - 1), self.dfs(l, r - 2))
        return max(chooseLeft, chooseRight)


print(Solution().predictTheWinner([1, 5, 233, 7, 3]))
print(Solution().predictTheWinner([1, 5, 2]))
