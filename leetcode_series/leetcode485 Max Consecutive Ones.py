# stupid question.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        if not nums:
            return 0

        maxcount = 0
        count = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
            maxcount = max(maxcount, count)

        return maxcount