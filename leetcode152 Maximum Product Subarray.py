
# O(N) time, O(1) Space.
# In interview, it's ok to first think of O(N) time & space solution, then optimize to O(1) space

class Solution(object):
    def maxProduct(self, nums):

        maximum, minimum = nums[0], nums[0]
        res = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                maximum, minimum = minimum, maximum
            maximum = max(nums[i] * maximum, nums[i])
            minimum = min(nums[i] * minimum, nums[i])
            res = max(maximum, res)

        return res



print Solution().maxProduct([-9, -4, 2, 7, -3, 8, 3])



'''
from copy import deepcopy

class Solution(object):
    def maxProduct(self, nums):

        if not nums:
            return 0
        
        minProductArray, maxProductArray = deepcopy(nums), deepcopy(nums)
        n = len(nums)
        
        for i in xrange(1, n):
            num = nums[i]
            if num == 0:
                continue
            elif num > 0:
                minProductEndsAtI = num * minProductArray[i - 1]
                maxProductEndsAtI = num * maxProductArray[i - 1]
            else:
                maxProductEndsAtI = num * minProductArray[i - 1]
                minProductEndsAtI = num * maxProductArray[i - 1]
            minProductArray[i] = min(num, minProductEndsAtI)
            maxProductArray[i] = max(num, maxProductEndsAtI)
        
        return max(max(minProductArray), max(maxProductArray))
'''