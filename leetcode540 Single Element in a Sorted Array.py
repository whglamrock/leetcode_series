from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        n = len(nums)
        while l <= r:
            m = (l + r) // 2
            if m - 1 >= 0 and nums[m] == nums[m - 1]:
                # target is in the left half
                if m % 2 == 0:
                    r = m - 2
                # target is in the right half
                else:
                    l = m + 1
            elif m + 1 < n and nums[m] == nums[m + 1]:
                if m % 2 == 0:
                    l = m + 2
                else:
                    r = m - 1
            else:
                return nums[m]

        # useless; just to avoid any syntax warnings
        return -1


print(Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(Solution().singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))
