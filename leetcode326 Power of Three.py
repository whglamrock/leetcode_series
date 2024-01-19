# the request is not using any loop/recursion. So it is definitely one of most stupid leetcode questions.
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3

        # 1 == 3 ^ 0, so if n == 1 it's also valid
        return True


'''
import math

# solution without using loop, but using built-in log function is essentially O(logN) time complexity
class Solution(object):
    def isPowerOfThree(self, n):

        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0
'''