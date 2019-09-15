
# Binary search solution: O(logN) where N == dividend / divisor.
# P.S.: We have to use Binary Manipulation to avoid "*"

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return
        if dividend == 0:
            return 0

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



# Taking (32, 5) as an example, the dividend goes through:
# 1) big while(1): 32 -> 27 -> 17;
# 2) big while(2): 17 -> 12 -> 2;
print Solution().divide(32, 5)















