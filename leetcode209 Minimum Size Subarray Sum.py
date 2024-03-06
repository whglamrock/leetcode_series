from typing import List

# O(N) sliding window solution. The O(N * log(N)) binary search solution is more straightforward (using prefix sum array)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = 2147483647
        l = 0
        subArraySum = 0
        for r, num in enumerate(nums):
            subArraySum += num
            while l <= r and subArraySum - nums[l] >= target:
                subArraySum -= nums[l]
                l += 1
            if subArraySum >= target:
                minLen = min(minLen, r - l + 1)

        return minLen if minLen != 2147483647 else 0
