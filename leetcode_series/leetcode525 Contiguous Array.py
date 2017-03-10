
# idea: set all zeroes to minus one; use accumulated presum

class Solution(object):
    def findMaxLength(self, nums):

        if not nums:
            return 0

        for i in xrange(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        maxlength = 0
        presum = 0
        dic = {0: -1}

        for i, num in enumerate(nums):
            presum += num
            if presum in dic:
                maxlength = max(maxlength, i - dic[presum])
            else:
                dic[presum] = i

        return maxlength