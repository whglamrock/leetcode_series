'''
One pass solution.
'''
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)/2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1

            # open the leetcode 33, 6 cases can correspond to the following, the big if and else both
            # represent 3 cases, both the small ifs represent 1 case and both small elses represent 2.
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # e.g. [4,5,6,7,0,1,2], target 6
                    r = mid - 1
                else:   # tricky case (in this case l == mid), e.g. [1,1,1,1,1,1,  1,3,3,4,1,1,1], target 3
                        # the part after the space is reserved after the above while loop, l == mid == 6, nums[l] == 1
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:  # e.g. [5,7,0,1,2,3,4], target 3
                    l = mid + 1
                else:   # tricky case, e.g. [1,1,1,  3,3,4,1,1,1,1,1,1,1], target 3. l = 3, mid = 6
                        # nums[l] == 3, nums[mid] == 1.
                    r = mid - 1
        return False

'''
# my orginal 'find the pivot first' solution, average o(logn) time complexity,
# worst case o(n) time complexity. Similar to the optimal solution but not done in one pass.

class Solution(object):
    def search(self, nums, target):

        def findpivot(nums):
            if len(nums) == 1:
                return 0
            if len(nums) == 2:
                return 1
            if len(nums) == 3:  # a bug corner case, only to deal with [1,1,1], not all 3-element cases.
                for i in xrange(2):
                    if nums[i] > nums[i+1]:
                        return i+1
                return 2

            l, r = 0, len(nums)-1
            while l <= r and l < len(nums) and r >=0:
                mid = (l+r)/2
                if nums[mid] == nums[-1]:   # freaky sick fuck case.
                    i = 0
                    while mid+i <= r and mid-i >= l and nums[mid+i] == nums[mid-i] == nums[-1]:
                        i += 1
                    if nums[mid-i] != nums[-1]:  # e.g. [1,1,3,4,1,1,1,1,1,1,1,1]
                        r = mid-i
                    elif nums[mid+i] != nums[-1]:  # e.g. [1,1,1,1,1,1,1,3,4,1,1,1]
                        l = mid+i
                    else:   # e.g. [1,1,1,1,1,1,1]
                        return mid

                elif nums[mid] < nums[-1]:
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
            return False
        else:
            return True
'''
