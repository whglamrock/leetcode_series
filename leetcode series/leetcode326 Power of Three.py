# the request is not using any loop/recursion. So it is definitely one of most stupid leetcode questions.
import math
class Solution(object):
    def isPowerOfThree(self, n):

        return n>0 and (math.log10(n)/math.log10(3))%1 == 0
