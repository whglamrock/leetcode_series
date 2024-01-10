from typing import List

# the simplest one pass O(logN) solution.
# P.S. comparing the nums[m] with nums[l] to divide the condition is easier than comparing nums[m] & target
# We need to notice that after a few loops the whole nums[l:r + 1] can be monotonically increasing
class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # instead of comparing nums[m] & target, we divide the condition by whether the left half is ascending
            # Note: the nums[l] == nums[m] is for case like nums = [3, 1], target = 1
            elif nums[l] <= nums[m]:  # ascending from l to m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # ascending from m to r
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


print(Solution().search([4, 5, 6, 7, 3], 3))


'''
# O(log(N)) find rotation pivot approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        indexOfPivot = self.findPivot(nums)
        if indexOfPivot == -1:
            return self.binarySearchTarget(nums, target, 0, len(nums) - 1)
        indexInLeft = self.binarySearchTarget(nums, target, 0, indexOfPivot)
        indexInRight = self.binarySearchTarget(nums, target, indexOfPivot + 1, len(nums) - 1)
        if indexInLeft == indexInRight == -1:
            return -1
        return max(indexInLeft, indexInRight)

    def binarySearchTarget(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        return -1
        
    def findPivot(self, nums: List[int]) -> int:
        # the nums is sorted, no rotation
        if nums[0] < nums[-1]:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if nums[l] > nums[l + 1]:
                    return l
                else:
                    return -1
            m = (l + r + 1) // 2
            if nums[m] >= nums[l]:
                l = m
            else:
                r = m - 1
        
        return l
'''