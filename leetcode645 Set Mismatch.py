
from copy import deepcopy

# not so efficient deepcopy way. However, it's O(1) space because it did not create another list
class Solution(object):
    def findErrorNums(self, nums):

        for i in xrange(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                indexDeepCopy = deepcopy(nums[i] - 1)
                tmp1, tmp2 = deepcopy(nums[i]), deepcopy(nums[nums[i] - 1])
                nums[i], nums[indexDeepCopy] = tmp2, tmp1

        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]



'''
class Solution(object):
    def findErrorNums(self, nums):

        numsSet = set(nums)
        dup = sum(nums) - sum(numsSet)
        for i in xrange(len(nums)):
            if i + 1 not in numsSet:
                return [dup, i + 1]
'''