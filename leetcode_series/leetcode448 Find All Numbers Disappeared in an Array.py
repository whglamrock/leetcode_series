
# idea: the nums[i] points to nums[nums[i]]. so mark nums[nums[i]] negative.
#   then those left positive are un-visited numbers.

class Solution(object):
    def findDisappearedNumbers(self, nums):

        if not nums:
            return []

        for i in xrange(len(nums)):
            # ue 'abs' because the nums[i] could be marked negative in previous loops
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        ans = []
        for i in xrange(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans