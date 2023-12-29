from typing import List

# sliding window solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        l, r = 0, 0
        currProduct = nums[0]
        while l < len(nums):
            # find the right index where the product of nums[l:r + 1]
            # is as big as possible but < k
            while r + 1 < len(nums) and nums[r + 1] * currProduct < k:
                currProduct *= nums[r + 1]
                r += 1
            # have to consider the possibility where l == r and nums[l] > k
            if currProduct < k:
                ans += r - l + 1
            # move the left index
            currProduct /= nums[l]
            l += 1
            # if the previous nums[l] is already > k or l == len(nums)
            if r < l:
                r = l
                if l < len(nums):
                    currProduct = nums[l]

        return ans


print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
print(Solution().numSubarrayProductLessThanK(nums=[10, 10, 10, 10], k=11))
