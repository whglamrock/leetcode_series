
'''
Binary Shift trick, in our case, we take (32,5) as an example
'''
# the dividend goes through: big while(1)32->27->17;big while(2)17->12->2;
# in every number after the "->" in the above line represent the new dividend after a little while.
# go through the entire loop to understand the algorithm.

class Solution:
    def divide(self, dividend, divisor):
        
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1 # in each big while, the temp has been reassigned the fixed divisor value.
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1

        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)



Sol = Solution()
print Sol.divide(32,5)















