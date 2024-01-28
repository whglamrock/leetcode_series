from math import ceil, factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nFactorial = factorial(n)
        ans = []
        nums = [i for i in range(1, n + 1)]
        for i in range(n, 0, -1):
            divider = nFactorial // i
            nFactorial = divider
            digit = nums[ceil(k / divider) - 1]
            ans.append(str(digit))
            nums.remove(digit)
            k %= divider

        return ''.join(ans)


print(Solution().getPermutation(9, 10000))
