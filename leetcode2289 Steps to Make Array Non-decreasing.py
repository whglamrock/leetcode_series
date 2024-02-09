from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] is the steps needed to remove nums[i]:
        # 1) If nums[i] == 1 it means nums[i] will be removed in the first run
        # 2) If nums[i] == 0 it means nums[i] is never removed (nums[i] >= all nums on its left)
        # 3) Initially assume all nums[i] can be removed in the first run. This is because for all nums[i] < nums[i - 1]
        # when we add them to decreasing stack it doesn't go through the while loop. Thus dp[i] will be 0 for them, while
        # in reality it still takes one (the very first) operation to remove them.
        dp = [1] * n
        # use a decreasing stack: if nums[i] >= some numbers in stack, those smaller numbers
        # will need to be removed before nums[i]. so dp[i] = max(dp[removedIndexes] + 1)
        stack = []
        for i, num in enumerate(nums):
            while stack and num >= stack[-1][1]:
                prevI, prevNum = stack.pop()
                dp[i] = max(dp[i], dp[prevI] + 1)

            # if there is no bigger number on left, need to reset dp[i] to 0
            if not stack:
                dp[i] = 0
            stack.append([i, num])

        return max(dp)


print(Solution().totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
print(Solution().totalSteps([4, 5, 7, 7, 13]))
