
'''
the whole point of this question is about returning the insert index when
target is not found
'''

class Solution(object):
    def searchInsert(self, nums, target):

        l, r = 0, len(nums)
        # exit condition is l == r
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if l < len(nums):
            if nums[l] < target:
                return l + 1
            else:
                return l
        else:
            return l