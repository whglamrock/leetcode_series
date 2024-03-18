from typing import List

# see discussion from: https://discuss.leetcode.com/topic/310/when-there-are-duplicates-the-worst-case-is-o-n-could-we-do-better
# 1337c0d3r gives the reason why we need to keep doing l += 1 when nums[l] == nums[mid]
# consider the tricky test case like:
#   nums = [1,1,1,1,1,1,  1,3,3,4,1,1,1], target 3
#   nums = [1,1,1,  3,3,4,1,1,1,1,1,1,1], target 3
#   worst case: nums = [1, 1, 1, 1, 1, 1, 1, 5], target = 5
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
                else:   # target > nums[m] or target < nums[l] (P.S., target could still == nums[l] due to duplicates)
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:   # target < nums[m] or target > nums[r] (P.S., target could still == nums[r] due to duplicates)
                    r = m - 1
            else:   # when l == m. it doesn't matter because in the next loop mid will be recalculated
                l += 1

        return False


print(Solution().search([1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1], 5))
print(Solution().search([1, 1, 1, 1, 1, 1, 1, 3, 3, 4, 1, 1, 1], 3))
