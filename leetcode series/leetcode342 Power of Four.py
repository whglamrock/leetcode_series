# as dumb as the 'power of three'

import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (math.log10(num)/math.log10(4))%1 == 0

# no need for fucking test cases
