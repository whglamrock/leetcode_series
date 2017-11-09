
# understand the definition of reservoir sampling
# know how to use random in python

import random

class Solution(object):

    def __init__(self, nums):

        self.nums = nums

    def pick(self, target):

        # initiate result as anything is okay since target is in the nums array
        result = -1
        count = 0

        for i, num in enumerate(self.nums):
            if self.nums[i] != target:
                continue
            count += 1
            if random.randrange(count) == 0:
                result = i

        return result



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)