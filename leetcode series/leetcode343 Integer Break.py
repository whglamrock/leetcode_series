# write down the biggest integer break from 2 to 15, you will be able to find out
class Solution(object):
    def integerBreak(self, n):

        if n == 2:
            return 1
        if n == 3:
            return 2

        ans = 1
        if n%3 == 0:
            for i in xrange(n/3):
                ans *= 3
        elif n%3 == 1:
            for i in xrange(n/3-1):
                ans *= 3
            ans *= 4
        elif n%3 == 2:
            for i in xrange(n/3):
                ans *= 3
            ans *= 2

        return ans