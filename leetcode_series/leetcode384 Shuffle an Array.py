# idea from: https://discuss.leetcode.com/topic/53985/well-explained-o-n-java-solution-by-using-random-class-and-swapping-current-with-a-random-previous-index
# swapping with previous indices.
import random
from copy import copy
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.index = [i for i in xrange(len(nums))]
        self.nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = copy(self.nums)
        for i in xrange(1, len(self.nums)):
            swapindex = random.randint(0, i)    # brilliant idea!
            ans[swapindex], ans[i] = ans[i], ans[swapindex]
        return ans
