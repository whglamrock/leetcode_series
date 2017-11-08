
# see discussion from: https://discuss.leetcode.com/topic/310/when-there-are-duplicates-the-worst-case-is-o-n-could-we-do-better
# 1337c0d3r gives the reason why we need to keep doing l += 1 when nums[l] == nums[mid]

# consider the tricky test case like:
#   nums = [1,1,1,1,1,1,  1,3,3,4,1,1,1], target 3
#   nums = [1,1,1,  3,3,4,1,1,1,1,1,1,1], target 3
#   worst case: nums = [1, 1, 1, 1, 1, 1, 1, 5], target = 5

class Solution(object):
    def search(self, nums, target):

        if not nums:
            return False
        l, r = 0, len(nums) - 1

        # the structure of this while loop is pretty much like lc
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return True
            # when there are more elements on the left of the pivot
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:   # target > nums[mid] or target < nums[l] (P.S., target could still == nums[l] due to duplicates)
                    l = mid + 1
            # when there are more elements on the right of the pivot
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:   # target < nums[mid] or target > nums[r] (P.S., target could still == nums[r] due to duplicates)
                    r = mid - 1
            else:   # even when l == mid. it doesn't matter because in the next loop mid will be recalculated
                l += 1

        return False



nums = [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1]
target = 5
Sol = Solution()
print Sol.search(nums, target)
