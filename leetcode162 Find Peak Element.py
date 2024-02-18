from typing import List

# we keep nums[l - 1] < nums[l] and nums[r + 1] < num[r], so [l:r + 1] is always the candidate area
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # we keep nums[l - 1] < nums[l] and nums[r] > nums[r + 1]
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m

        return l


print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(Solution().findPeakElement([1, 2, 3, 1]))
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 1]))
print(Solution().findPeakElement([1, 2]))
