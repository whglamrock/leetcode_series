
# what's the fucking point of such question?
# idea from: https://leetcode.com/problems/count-good-numbers/solutions/1314363/java-python-3-iterative-o-logn-code-similar-to-lc50-pow-x-n-w-brief-explanation-and-analysis/
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def countGood(power: int, x: int) -> int:
            if power == 0:
                return 1
            elif power % 2 == 0:
                return countGood(power // 2, x * x % MOD)
            return x * countGood(power - 1, x) % MOD

        MOD = 10 ** 9 + 7
        return 5 ** (n % 2) * countGood(n // 2, 4 * 5) % MOD
