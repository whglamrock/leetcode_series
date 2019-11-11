
# The key is to remember to set the 0 to -1 and use preSum. Otherwise solely using dp without hashMap won't work

class Solution(object):
    def findMaxLength(self, nums):

        if not nums:
            return 0

        for i in xrange(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        maxLen = 0
        preSum = 0
        preSumToIndex = {0: -1}

        for i, num in enumerate(nums):
            preSum += num
            if preSum in preSumToIndex:
                maxLen = max(maxLen, i - preSumToIndex[preSum])
            else:
                preSumToIndex[preSum] = i

        return maxLen



print Solution().findMaxLength([0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])