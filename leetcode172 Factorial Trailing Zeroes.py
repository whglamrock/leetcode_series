# idea: https://leetcode.com/problems/factorial-trailing-zeroes/solutions/52367/my-explanation-of-the-log-n-solution/
# Taking 125 as an example, within 125, there are 125/5 = 25 numbers provide a factor of 5 (ends with 5). But those
# numbers that are multiple of 25 will provide one extra 5 (i.e., 25, 50, 75, 100, 125) because for example
# 50 = 5 * 5 * 2. Same idea for 125 = 5 * 5 * 5. So we can come up with the recursive solution
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)


print(Solution().trailingZeroes(5))
