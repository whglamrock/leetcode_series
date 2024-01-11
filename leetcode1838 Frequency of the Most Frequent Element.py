from typing import List

# use for loop instead of while loop to implement the sliding window
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        windowSum = 0
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            windowSum += num
            while k < num * (r - l + 1) - windowSum:
                windowSum -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)

        return ans


print(Solution().maxFrequency(nums=[1, 2, 4], k=5))
print(Solution().maxFrequency(nums=[1, 4, 8, 13], k=5))
print(Solution().maxFrequency(nums=[3, 9, 6], k=2))
