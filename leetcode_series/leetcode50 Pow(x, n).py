
# O(logN) running time solution

class Solution(object):
    def myPow(self, x, n):

        if n == 0: return 1

        if n < 0:
            n = -n
            x = 1 / x

        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)



Sol = Solution()
x = 1.00012
n = 1024
print Sol.myPow(x, n)

