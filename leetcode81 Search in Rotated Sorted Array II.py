from typing import List

# See discussion from: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/28212/when-there-are-duplicates-the-worst-case-is-on-could-we-do-better/,
# 1337c0d3r gives the reason why we need to keep doing l += 1 when nums[l] == nums[m]
# Consider the tricky test case like:
# 1) nums = [1,1,1,1,1,1,  1,3,3,4,1,1,1], target 3
# 2) nums = [1,1,1,  3,3,4,1,1,1,1,1,1,1], target 3
# 3) worst case: nums = [1, 1, 1, 1, 1, 1, 1, 5], target = 5
class Solution(object):
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # target > nums[m] or target < nums[l] (P.S., target could still == nums[l] due to duplicates)
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # target < nums[m] or target > nums[r] (P.S., target could still == nums[r] due to duplicates)
                else:
                    r = m - 1
            else:
                l += 1

        return False


print(Solution().search([1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1], 5))
print(Solution().search([1, 1, 1, 1, 1, 1, 1, 3, 3, 4, 1, 1, 1], 3))
