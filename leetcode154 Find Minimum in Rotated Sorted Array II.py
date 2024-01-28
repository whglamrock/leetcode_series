from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return nums[m]
            # not rotated
            if nums[l] < nums[r]:
                return nums[l]
            # rotated
            elif nums[l] > nums[r]:
                if nums[m] <= nums[r]:
                    r = m
                else:
                    l = m + 1
            # nums[l] == nums[r] could be rotated or not
            # if it's not rotated, there is only 1 possibility where all nums[i] are equal
            else:
                if nums[m] < nums[r]:
                    r = m
                elif nums[m] > nums[r]:
                    l = m + 1
                else:
                    return self.moveLeftOrRightToFindMin(nums, m)

    def moveLeftOrRightToFindMin(self, nums: List[int], i: int) -> int:
        minValue = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] > minValue:
                break
            minValue = min(minValue, nums[j])
        for j in range(i - 1, -1, -1):
            if nums[j] > minValue:
                break
            minValue = min(minValue, nums[j])
        return minValue


print(Solution().findMin([4, 4, 4, 4, 4, 4, 4, 0, 1, 1, 3, 4, 4]))
print(Solution().findMin([4, 4, 4, 4, 0, 1, 1, 3, 4, 4, 4, 4]))
print(Solution().findMin([4, 4, 4, 4, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
print(Solution().findMin([4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
