from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        currSum = sum(nums[:k])
        maxSum = currSum

        for i in range(k, n):
            currSum -= nums[i - k]
            currSum += nums[i]
            maxSum = max(currSum, maxSum)

        return maxSum / k


print(Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(Solution().findMaxAverage(nums=[5], k=1))
