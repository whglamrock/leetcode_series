
# see discussion from: https://discuss.leetcode.com/topic/310/when-there-are-duplicates-the-worst-case-is-o-n-could-we-do-better
# 1337c0d3r gives the reason why we need to keep doing l += 1 when nums[l] == nums[mid]

class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1

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



nums = [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1]
# an example of worst case: nums = [1, 1, 1, 1, 1, 1, 1, 5]
target = 5
Sol = Solution()
print Sol.search(nums, target)
