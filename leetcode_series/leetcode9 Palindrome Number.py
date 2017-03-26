
# in the lc OJ, all negative numbers should be returned false

class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        original = x
        count = 0
        while original:
            original /= 10
            count += 1

        for i in xrange(count/2):
            if (x / pow(10, i)) % 10 != (x / pow(10, count - i - 1)) % 10:
                return False

        return True