
# idea from: https://discuss.leetcode.com/topic/53985/well-explained-o-n-java-solution-by-using-random-class-and-swapping-current-with-a-random-previous-index
# swapping with previous indices.

import random
from copy import copy

class Solution(object):

    def __init__(self, nums):

        self.index = [i for i in xrange(len(nums))]
        self.nums = nums


    def reset(self):

        return self.nums


    def shuffle(self):

        ans = copy(self.nums)
        for i in xrange(1, len(self.nums)):
            swapindex = random.randint(0, i)    # brilliant idea!
            ans[swapindex], ans[i] = ans[i], ans[swapindex]
        return ans
