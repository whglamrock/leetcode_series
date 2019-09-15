
# Binary search solution: O(logN) where N == dividend / divisor.
# P.S.: We have to use Binary Manipulation to avoid "*"

class Solution:
    def divide(self, dividend, divisor):

        if divisor == 0:
            return
        if dividend == 0:
            return 0

        positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1

        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)



# Taking (32, 5) as an example, the dividend goes through:
# 1) big while(1): 32 -> 27 -> 17;
# 2) big while(2): 17 -> 12 -> 2;
print Solution().divide(32, 5)















