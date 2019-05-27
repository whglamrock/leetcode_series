
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

    # use recursion to do the binary scale down job
    # we assume n is positive right here
    def fastPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        half = self.fastPow(x, n / 2)
        if n % 2 == 0:
            return half * half
        else:
            # note that we still consider this extra 'x *' step as idempotent, so overall time complexity is logN
            return x * half * half



Sol = Solution()
x = 1.00012
n = 1024
print Sol.myPow(x, n)

