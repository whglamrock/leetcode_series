from typing import List


class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        currSum = sum(nums[:k])
        count = 1 if currSum >= k * threshold else 0
        for i in range(k, len(nums)):
            currSum = currSum - nums[i - k] + nums[i]
            if currSum >= k * threshold:
                count += 1

        return count
