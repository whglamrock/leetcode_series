
# -*- coding: utf-8 -*-
# ONE-PASS o(logn) solution
# idea came from: https://discuss.leetcode.com/topic/47785/1-pass-binary-search-in-python-11-lines-50-ms
# Three cases of (lv, mv, rv) relationship (假设减小的那一个值为pivot):
#   1. lv < mv < rv (单调递增):
#       target在mid的右边 —— mv < target < lv;
#       target在mid的左边 —— lv < target < mv;
#   2. mv < rv < lv (在pivot右边有more elements):
#       target在mid的右边 —— mv < target < rv;
#       target在mid的左边 —— target < mv or target > lv;
#   3. rv < lv < mv (在pivot左边有more elements)
#       target在mid的右边 —— target < rv or target > mv;
#       target在mid的左边 —— lv < target < mv;
# 以上8种情况可以归纳成3种if—else的条件,如下:

class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1

        while left<=right:
            mid = left+(right-left)/2
            lv, mv, rv = nums[left], nums[mid], nums[right]

            if lv < target < mv or mv < lv < target or target < mv <rv:
                right = mid-1
            elif lv < mv < target or target < rv < mv or mv < target < rv:
                left = mid+1
            else:
                break   # means the target == one of (lv, mv, rv)

        if target == lv:
            return left
        elif target == mv:
            return mid
        elif target == rv:
            return right
        else:
            return -1



'''
# Another more simple, one pass solution came from leetcode 88.
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
'''



'''
# my original two-pass but still o(logn) solution:
class Solution(object):
    def search(self, nums, target):

        def findpivot(nums):
            l, r = 0, len(nums)-1
            while l <= r and l < len(nums)-1 and r >=0:
                mid = (l+r)/2
                if nums[mid] < nums[-1]:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        def binarysearch(nums, start, end, target):
            l, r = start, end
            while l <= r:
                mid = (l+r)/2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1

        pivot = findpivot(nums)
        if binarysearch(nums, 0, pivot-1, target) == binarysearch(nums, pivot, len(nums)-1, target) == -1:
            return -1
        else:
            return max(binarysearch(nums, 0, pivot-1, target),binarysearch(nums, pivot, len(nums)-1, target))
'''