
# Binary search solution: O(logN) where N == dividend / divisor. We have to use bit Manipulation to avoid "*"
class Solution(object):
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        ans = 0
        while dividend >= divisor:
            tmp = divisor
            i = 1
            while dividend >= tmp:
                dividend -= tmp
                ans += i
                tmp <<= 1
                i <<= 1

        ans = ans if positive else -ans
        return max(min(ans, 2147483647), -2147483648)


print(Solution().divide(32, 5))
