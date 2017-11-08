
# idea came from: https://discuss.leetcode.com/topic/4417/possibly-simplest-solution-with-o-n-time-complexity
# O(N) time, O(1) Space.

class Solution(object):
    def maxProduct(self, nums):

        maximum, minimum = nums[0], nums[0]
        res = nums[0]
        for i in xrange(1, len(nums)):  # i has to start from 1, or the nums[0]*nums[0] means duplication
            if nums[i] < 0:
                maximum, minimum = minimum, maximum  # if nums[i] < 0: nums[i]*maximum will be the min;
                # nums[i]*minimum will be the max.
            maximum = max(nums[i]*maximum, nums[i])
            minimum = min(nums[i]*minimum, nums[i])
            res = max(maximum, res)

        return res



Sol = Solution()
nums = [-9,-4,2,7,-3,8,3]
print(Sol.maxProduct(nums))

