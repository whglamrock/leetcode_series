
# Description: http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/

class Solution(object):
    # n is number of eggs initialized, k is number of floors.
    def eggDrop(self, n, k):

        if k == 1 or k == 0:
            return k

        if n == 1:
            return k

        mininmum = 2147483647
        for i in xrange(1, k + 1):
            res = max(self.eggDrop(n - 1, i - 1), self.eggDrop(n, k - i))
            if res < mininmum:
                mininmum = res

        #print n, k, mininmum + 1
        return mininmum + 1



Sol = Solution()
print Sol.eggDrop(2, 20)
