from typing import List, Dict


class Solution(object):
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        nums = [i for i in range(1, maxChoosableInteger + 1)]
        return self.dfs(nums, desiredTotal, {})

    def dfs(self, nums: List[int], desiredTotal: int, memo: Dict[str, bool]) -> bool:
        key = str(nums)
        if key in memo:
            return memo[key]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            # if we want the current player to win, the next round (the other player) must not win
            if not self.dfs(nums[:i] + nums[i + 1:], desiredTotal - nums[i], memo):
                memo[key] = True
                return True

        memo[key] = False
        return False
