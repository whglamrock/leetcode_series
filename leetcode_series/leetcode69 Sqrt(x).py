
class Solution(object):
    def mySqrt(self, x):

        l, r = 0, x
        # exit condition: l == r
        while l < r:
            mid = l + (r - l) / 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:   # x > (mid + 1) * (mid + 1)
                l = mid + 1

        return l



a = 20
Sol = Solution()
b = Sol.mySqrt(a)
print b






