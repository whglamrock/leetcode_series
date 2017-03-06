# Hard level problem. Idea from: https://discuss.leetcode.com/topic/49751/clear-explanation-of-why-using-gcd/2
class Solution(object):
    def canMeasureWater(self, x, y, z):

        def gcd(x, y):  # get the 'greatest common divisor'
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        return z == 0 or (z <= x + y and z % gcd(x, y) == 0)