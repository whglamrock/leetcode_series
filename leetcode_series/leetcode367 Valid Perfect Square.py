# idea: binary search
class Solution(object):
    def isPerfectSquare(self, num):

        if (not num) or num < 0: return False
        if num == 1: return True

        l, r = 0, num/2
        while l <= r:
            mid = (l + r) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1

        if l * l == num or r * r == num: return True
        return False