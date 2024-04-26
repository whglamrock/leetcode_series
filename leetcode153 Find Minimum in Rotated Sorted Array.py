from typing import List

# based on the question, sorted in "ascending" order means there is no duplicates
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # l to r is increasing (sorted)
            if nums[l] < nums[r]:
                return nums[l]
            # nums[l] > nums[r]
            else:
                # when nums[m] == nums[l], it's l == m
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m

        return nums[l]


print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
