
# pay attention that we should only return 0 when ans (not original x) overflows

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        positive = x > 0
        x = abs(x)

        ans = 0
        while x:
            ans = ans * 10 + (x % 10)
            x /= 10

        if not positive:
            ans = -ans
        return ans if -2147483648 <= ans <= 2147483647 else 0