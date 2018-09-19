
#  "l <= r" solution

class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1



'''
class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        return -1
'''