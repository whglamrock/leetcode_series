from typing import List

# the simplest one pass O(logN) solution.
# P.S. comparing the nums[m] with nums[l] to divide the condition is easier than comparing nums[m] & target
# We need to notice that after a few loops the whole nums[l:r + 1] can be monotonically increasing
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] == target:
                    return m
                return -1

            # instead of comparing nums[m] & target, we divide the condition by whether the left half is ascending
            # Note: the nums[l] == nums[m] is for case like nums = [3, 1], target = 1
            if nums[l] <= nums[m]:  # ascending from l to m
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:  # ascending from m to r
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m

        return -1


print(Solution().search([4, 5, 6, 7, 3], 3))
