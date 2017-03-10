# idea from ugly number: https://discuss.leetcode.com/topic/23893/my-expressive-python-solution
# O(mn) solution
from copy import copy
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):

        ugly = [1]
        u = copy(primes)
        iu = [0] * len(primes)

        while n > 1:
            umin = min(u)
            add = []
            for i in xrange(len(primes)):
                if u[i] == umin:    # not to break here, if multiple u[i]s equal to umin, we need to update
                    iu[i] += 1    # all iu[i]s to avoid duplicates
                    add.append(i)
            ugly.append(umin)
            for index in add:
                u[index] = primes[index] * ugly[iu[index]]
            n -= 1

        #print ugly
        return ugly[-1]


Sol = Solution()
primes = [2,7,13,19]
print Sol.nthSuperUglyNumber(8,primes)
