
# -*- coding: utf-8 -*-
# Binary search find the 'maximum' value
# It isn't the actual maximum but will "peak": the left/right element smaller than it.

class Solution(object):
    def findPeakElement(self, nums):

        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)/2
            midd = mid+1
            if nums[mid]<nums[midd]:
                l = midd
            else:
                r = mid

        return l

# nums[l:r + 1] are candidates. The element right on the left of nums[l] is smaller than
# nums[l], the element right on the right of nums[r] smaller than nums[r].
# If nums[l] != nums[r], then after every iteration, nums[l] or nums[r] will always be
# candidates. Even if nums[l] could == nums[r], at last they won't equal to each other
# when r == l + 1 because nums[i] != nums[i + 1].