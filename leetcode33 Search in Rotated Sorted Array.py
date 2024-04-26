from typing import List

# reusing the code from lc153. It's less error-prone and takes less thought time in real interview, although you
# need to write more code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findMin(nums)
        left, right = self.findTarget(nums, target, 0, minIndex - 1), self.findTarget(nums, target, minIndex, len(nums) - 1)
        if left == right == -1:
            return -1

        return max(left, right)

    def findTarget(self, nums: List[int], target: int, l: int, r: int):
        if not nums:
            return -1

        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] == target:
                    return m
                return -1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

    # reusing code in lc153
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # nums[l:r + 1] is ascending
            if nums[l] < nums[r]:
                return l
            # nums[l] > nums[r] since l != r
            else:
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m

        return l


print(Solution().search([4, 5, 6, 7, 3], 3))
