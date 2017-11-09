
class Solution(object):
    def numWays(self, n, k):

        if n == 0:
            return 0
        elif n == 1:
            return k

        same = k
        dif = k*(k-1)

        for i in xrange(3, n+1):
            same, dif = dif, (same+dif)*(k-1)

        return same+dif



Sol = Solution()
print Sol.numWays(43,2)







