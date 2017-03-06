# understand the definition of reservoir sampling
# know how to use random in python
import random
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = -1
        count = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] != target:
                continue
            count += 1
            if random.randrange(count) is 0:  # 'is 0' is faster than '== 0'
                result = i

        return result



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)