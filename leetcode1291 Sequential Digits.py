from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        twoDigit = [12, 23, 34, 45, 56, 67, 78, 89]
        threeDigit = [123, 234, 345, 456, 567, 678, 789]
        fourDigit = [1234, 2345, 3456, 4567, 5678, 6789]
        fiveDigit = [12345, 23456, 34567, 45678, 56789]
        sixDigit = [123456, 234567, 345678, 456789]
        sevenDigit = [1234567, 2345678, 3456789]
        eightDigit = [12345678, 23456789]
        nineDigit = [123456789]

        sequentialDigitNums = twoDigit + threeDigit + fourDigit + fiveDigit + sixDigit + sevenDigit + eightDigit + nineDigit
        ans = []
        for num in sequentialDigitNums:
            if low <= num <= high:
                ans.append(num)
        return ans
