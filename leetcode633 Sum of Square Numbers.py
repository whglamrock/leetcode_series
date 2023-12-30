from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        upperBound = int(sqrt(c)) + 1
        for i in range(upperBound):
            sqrtOfResidual = sqrt(c - i * i)
            if sqrtOfResidual == int(sqrtOfResidual):
                return True

        return False


print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(85))
print(Solution().judgeSquareSum(3))
print(Solution().judgeSquareSum(0))
