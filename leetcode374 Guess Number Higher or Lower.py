
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        l, r = 1, n
        while l <= r:
            m = (l + r) / 2
            if guess(m) == 0:
                return m
            # m < target
            elif guess(m) == 1:
                l = m + 1
            else:
                r = m - 1

