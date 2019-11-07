
class Solution(object):
    def mySqrt(self, x):

        l, r = 0, x
        # exit condition: l == r
        while l < r:
            m = l + (r - l) / 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            elif x < m * m:
                r = m - 1
            else:   # x > (mid + 1) * (mid + 1)
                l = m + 1

        return l



print Solution().mySqrt(20)






