
class Solution(object):
    def mySqrt(self, x):

        left, right = 0, x
        while left <= right:
            mid = int((left+right)/2)
            if mid ** 2 <= x < (mid+1) ** 2:
                return mid
            elif mid ** 2 > x:
                right = mid
            else:
                left = mid + 1



a = 1
Sol = Solution()
b = Sol.mySqrt(a)
print b






