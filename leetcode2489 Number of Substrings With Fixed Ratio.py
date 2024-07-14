from collections import defaultdict


# Intuition:
# 1) Assume the substring we want is s[i:j], the number if zeroes in s[:i] and s[:j] are x1 and x2; thee number of ones
# in s[:i] and s[:j] are y1 and y2.
# 2) We have (x2 - x1) / (y2 - y1) = num1 / num2 ==> (y2 - y1) * num1 = (x2 - x1) * num2
# ==> y2 * num1 - x2 * num2 = y1 * num1 - x1 * num2
# 3) So naturally, we need to calculate the y * num1 - x * num2 of each prefix.
class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        zero, one = 0, 0
        dp = defaultdict(int)
        # this is for easy calculation when we wanna consider the entire prefix as a ratio substr
        dp[0] = 1
        ans = 0
        for digit in s:
            if digit == '0':
                zero += 1
            else:
                one += 1

            ans += dp[one * num1 - zero * num2]
            dp[one * num1 - zero * num2] += 1

        return ans
