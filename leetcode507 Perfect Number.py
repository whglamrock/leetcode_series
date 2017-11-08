
from math import sqrt

class Solution(object):
    def checkPerfectNumber(self, num):

        if num <= 0:
            return False

        divisors = set()
        for i in xrange(1, int(sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num / i)

        divisors.discard(num)
        return sum(divisors) == num



Sol = Solution()
print Sol.checkPerfectNumber(28)
print Sol.checkPerfectNumber(14)

