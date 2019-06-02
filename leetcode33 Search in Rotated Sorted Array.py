
# the simplest one pass solution.
# comparing the nums[mid] with nums[l] to divide the condition is easier than comparing nums[m] & target

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
            m = l + (r - l) / 2
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



nums = [4, 5, 6, 7, 3]
target = 3
Sol = Solution()
print Sol.search(nums, target)



'''
# upper bound being n solution, still O(logN)

class Solution(object):
    def search(self, nums, target):
    
        if not nums:
            return -1
        
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) / 2
            if nums[m] == target:
                return m
            # means it's ascending from l to m
            elif nums[l] <= nums[m]:
                if target > nums[m]:
                    l = m + 1
                # target < nums[m]
                else:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m
            # means it's ascending from m to r
            else:
                if target < nums[m]:
                    r = m
                # target > nums[m]
                else:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m
        
        return -1  
'''


