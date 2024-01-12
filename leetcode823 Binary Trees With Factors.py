from typing import List

# for each nums[i], calculate the number of possible products
class Solution:
    def numFactoredBinaryTrees(self, nums: List[int]) -> int:
        nums.sort()
        numToIndex = {}
        for i, num in enumerate(nums):
            numToIndex[num] = i

        n = len(nums)
        dp = [1] * n
        mod = 10 ** 9 + 7
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] != 0:
                    continue
                if nums[j] * nums[j] == nums[i]:
                    dp[i] += dp[j] * dp[j]
                    dp[i] %= mod
                elif nums[i] // nums[j] in numToIndex:
                    dp[i] += dp[j] * dp[numToIndex[nums[i] // nums[j]]]
                    dp[i] %= mod

        return sum(dp) % mod


print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))
print(Solution().numFactoredBinaryTrees([2, 4, 5, 10, 40, 100]))
print(Solution().numFactoredBinaryTrees(
    [242, 315, 26, 27, 16, 337, 75, 371, 253, 67, 105, 327, 96, 373, 113, 167, 3, 99, 193]))
