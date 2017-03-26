
# compare the bit one by one from the least to most significant

class Solution(object):
    def hammingDistance(self, x, y):

        ans = 0
        while x or y:
            rightmostbitofx = x & 1
            rightmostbitofy = y & 1
            if rightmostbitofx != rightmostbitofy:
                ans += 1
            x >>= 1
            y >>= 1

        return ans