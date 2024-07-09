class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        possibleSqrt = self.findSqrtEqualOrSmaller(num)
        return possibleSqrt * possibleSqrt == num

    def findSqrtEqualOrSmaller(self, num: int) -> int:
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return m

            if m * m == num:
                return m
            elif m * m < num:
                l = m + 1
            else:
                r = m - 1

        return l
