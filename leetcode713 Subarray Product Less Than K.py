from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        currProduct = 1
        ans = 0
        for r, num in enumerate(nums):
            currProduct *= num
            while currProduct >= k and l <= r:
                currProduct //= nums[l]
                l += 1
            if currProduct < k:
                ans += r - l + 1

        return ans


print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
print(Solution().numSubarrayProductLessThanK(nums=[10, 10, 10, 10], k=11))
