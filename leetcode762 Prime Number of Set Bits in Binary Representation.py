
class Solution(object):
    def countPrimeSetBits(self, L, R):

        sumOfPrimeSets = 0
        for i in xrange(L, R + 1):
            if bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19]:
                sumOfPrimeSets += 1

        return sumOfPrimeSets



print Solution().countPrimeSetBits(842, 888)
