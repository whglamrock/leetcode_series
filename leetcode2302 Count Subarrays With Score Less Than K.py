from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        subarraySum = 0
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            subarraySum += num
            while subarraySum * (r - l + 1) >= k:
                subarraySum -= nums[l]
                l += 1
            if r >= l:
                ans += r - l + 1

        return ans


print(Solution().countSubarrays(nums=[2, 1, 4, 3, 5], k=10))
print(Solution().countSubarrays(nums=[1, 1, 1], k=5))
