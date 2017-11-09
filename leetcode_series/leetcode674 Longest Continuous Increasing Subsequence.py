
class Solution(object):
    def findLengthOfLCIS(self, nums):

        # not sure whether we should return 0 or throw exception when nums is None
        if not nums:
            return 0

        maxLen = 1
        currLen = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currLen += 1
            else:
                currLen = 1
            maxLen = max(maxLen, currLen)

        return maxLen