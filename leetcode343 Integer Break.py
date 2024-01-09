
# write down the biggest integer break from 2 to 15, you will be able to find out
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 3:
            return 2
        if n == 2:
            return 1

        ans = 1
        if n % 3 == 0:
            for i in range(n // 3):
                ans *= 3
        elif n % 3 == 1:
            for i in range(n // 3 - 1):
                ans *= 3
            ans *= 4
        # n % 3 == 2
        else:
            for i in range(n // 3):
                ans *= 3
            ans *= 2

        return ans


print(Solution().integerBreak(23))
print(Solution().integerBreak(10))
