from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return nums[m]
            # l to r is increasing (i.e., sorted)
            if nums[l] < nums[r]:
                return nums[l]
            # nums[l] > nums[r]
            else:
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m

        return nums[l]


print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
