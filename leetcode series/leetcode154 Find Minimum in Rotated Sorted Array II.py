class Solution(object):
    def findMin(self, nums):

        if (not nums) or len(nums) == 0:
            return

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[r]:  # nums[mid] can't be the answer
                l = mid + 1
            elif nums[mid] < nums[r]:  # nums[mid] could be the answer
                r = mid
            else:
                r -= 1

        return nums[l]  # return nums[r] is the same.

# extreme cases like [10, 1, 10, 10, 10] and [10, 10, 10, 1, 10] are very
# important

'''
# the following code has problem for test case like [10, 1, 10, 10, 10]:
class Solution(object):
    def findMin(self, nums):

        if (not nums) or len(nums) == 0:
            return

        l, r = 0, len(nums) - 1
        while l < r:
            #print l, r
            mid = l + (r - l) / 2
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                l += 1

        return nums[l]

# because for "nums[mid] > nums[r]" we can absolutely be sure that we need to
# move left. But for "nums[mid] > nums[l]" we can't. For example, in these two cases:
# [4,5,6,7,0,1,2] and [1, 10, 10, 10], both satisfy nums[mid] > nums[l], but we could
# move to mid's left or right. But nums[mid] > nums[r] doesn't have this problem, for
# [4,5,6,7,0,1,2] and [10, 10, 10, 1], both move to the right.

'''