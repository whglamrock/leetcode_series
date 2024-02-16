from typing import List

# Be careful about the edge case like nums = [0, 0, 0] and target = 0. We have to update indexToClosestLeftIndex
# in the same for loop of building prefixSum to index.
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefixSumToIndex = {}
        currSum = 0
        prefixSums = []
        indexToClosestLeftIndex = {}
        for i, num in enumerate(nums):
            currSum += num
            if currSum == target:
                indexToClosestLeftIndex[i] = 0
            if currSum - target in prefixSumToIndex:
                indexToClosestLeftIndex[i] = prefixSumToIndex[currSum - target] + 1
            # update the prefixSumToIndex at last
            prefixSumToIndex[currSum] = i
            prefixSums.append(currSum)

        dp = [0] * len(nums)
        for i in range(len(nums)):
            # need to populate the previous state and compare maximum instead of
            # directly setting dp[i] = 1 + dp[closestLeftIndex - 1]
            if i - 1 >= 0:
                dp[i] = dp[i - 1]
            if i not in indexToClosestLeftIndex:
                continue

            closestLeftIndex = indexToClosestLeftIndex[i]
            if closestLeftIndex - 1 >= 0:
                dp[i] = max(1 + dp[closestLeftIndex - 1], dp[i])
            else:
                dp[i] = max(1, dp[i])

        return max(dp)


print(Solution().maxNonOverlapping([-1, -2, 8, -3, 8, -5, 5, -4, 5, 4, 1], 5))
print(Solution().maxNonOverlapping([0, 0, 0], 0))
