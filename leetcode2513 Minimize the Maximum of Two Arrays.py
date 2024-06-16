from math import lcm

# 1) Draw a pie chart (a pie of all numbers, and subset for numbers that are divisible for 1 and divisible for 2)
# 2) Any number that's not divisible by lcm(d1, d2) can be candidate to reduce either unique count
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = 1, 10 ** 10
        leastCommonMultiple = lcm(divisor1, divisor2)

        while l < r:
            m = (l + r) // 2

            distinctNumsForDivisor1 = m - m // divisor1
            distinctNumsForDivisor2 = m - m // divisor2
            distinctNumsForBoth = m - m // leastCommonMultiple
            if distinctNumsForDivisor1 >= uniqueCnt1 and distinctNumsForDivisor2 >= uniqueCnt2 and distinctNumsForBoth >= (uniqueCnt1 + uniqueCnt2):
                r = m
            else:
                l = m + 1

        return l
