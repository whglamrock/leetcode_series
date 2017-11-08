
# Idea: find the target value first, then search the start in left area, the end in right area.

class Solution(object):
    def searchRange(self, nums, target):
        l, r = 0, len(nums)-1
        index = None
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1

        if index == None:
            return [-1,-1]

        l1, r1 = 0, index
        l2, r2 = index, len(nums)-1
        start, end = None, None
        while l1 <= r1:
            mid = (l1+r1)/2
            if nums[mid] == target:
                if mid-1 >= 0:
                    r1 = mid-1
                else:
                    start = mid
                    break
            else:
                if mid+1 < len(nums) and nums[mid+1] == target:
                    start = mid+1
                    break
                else:
                    l1 = mid+1

        while l2 <= r2:
            mid = (l2+r2)/2
            if nums[mid] == target:
                if mid+1 < len(nums):
                    l2 = mid+1
                else:
                    end = mid
                    break
            else:
                if mid-1 >= 0 and nums[mid-1] == target:
                    end = mid-1
                    break
                else:
                    r2 = mid-1

        if start != None and end != None:
            return [start, end]
        else:
            return [index, index]



Sol = Solution()
nums = [2,2]
target = 2
print Sol.searchRange(nums, target)