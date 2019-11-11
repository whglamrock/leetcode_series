
# the simplest one pass O(logN) solution.
# P.S. comparing the nums[m] with nums[l] to divide the condition is easier than comparing nums[m] & target
    # We need to notice that after a few loops the whole nums[l:r + 1] can be monotonically increasing

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
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



print Solution().search([4, 5, 6, 7, 3], 3)



'''
# the "l < r while condition" solution 

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            # it means [l:r + 1] is monotonously increasing 
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            # nums[l] > nums[r] because there is no duplicates
            else:
                # nums[l:m + 1] is monotonously increasing 
                if nums[l] <= nums[m]:
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        
        return l if nums[l] == target else -1
'''