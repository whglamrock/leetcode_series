
# need to think of divide and conquer idea (fastPow)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.fastPow(x, -n)
        else:
            return self.fastPow(x, n)

    def fastPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half


print(Solution().myPow(1.00012, 1024))
print(Solution().myPow(3.2, 10))

