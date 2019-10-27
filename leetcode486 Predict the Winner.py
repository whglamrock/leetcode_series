
# dfs + memo. Dp idea is actually hard to implement and more error-prone in real interview
# The total number of subproblems is N^2, but the time complexity is not O(N^2). We can use a count variable to count
    # how many times the dfs method is invoked

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        n = len(nums)
        bestScore = self.dfs(nums, 0, n - 1, {})

        return 2 * bestScore >= sum(nums)

    # dfs gets the max score a player can get from nums[i:j + 1]
    def dfs(self, nums, i, j, memo):

        if i > j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        # nums[i + 1:j + 1] remains and the next player can choose nums[i + 1] or nums[j]
        chooseLeft = nums[i] + min(self.dfs(nums, i + 2, j, memo), self.dfs(nums, i + 1, j - 1, memo))
        # nums[i:j + 1] remains and the next player can choose nums[i] or nums[j - 1]
        chooseRight = nums[j] + min(self.dfs(nums, i + 1, j - 1, memo), self.dfs(nums, i, j - 2, memo))

        res = max(chooseLeft, chooseRight)
        memo[(i, j)] = res

        return res



print Solution().PredictTheWinner([1, 5, 233, 7, 3])
print Solution().PredictTheWinner([1, 5, 2])