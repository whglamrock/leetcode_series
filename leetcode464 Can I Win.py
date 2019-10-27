
# Basic DFS solution with memoization.
# We need to think of using a newly built list with the used number removed and use str(newNums) as key of memo

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        nums = range(1, maxChoosableInteger + 1)
        return self.helper(nums, desiredTotal, {})

    def helper(self, nums, desiredTotal, memo):

        # python cannot directly use list as key
        key = str(nums)
        if key in memo:
            return memo[key]

        # means this player can choose at least one number to get a win
        if nums[-1] >= desiredTotal:
            return True

        # the length of nums could change
        for i in xrange(len(nums)):
            # instead of using a used list to pass through recursion, build a list with the used number removed
            if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i], memo):
                memo[key] = True
                return True

        memo[key] = False
        return False



print Solution().canIWin(11, 43)
print Solution().canIWin(10, 11)