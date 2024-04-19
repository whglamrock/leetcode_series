from typing import List

# most likely in real interview the motherfucking interviewer will ask for in-place swap
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]

        return nums
