
# notice how we deal with when n % 2 != 0

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.fastPow(x, -n)
        else:
            return self.fastPow(x, n)

    def fastPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        half = self.fastPow(x, n / 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half



print Solution().myPow(1.00012, 1024)
print Solution().myPow(3.2, 10)

