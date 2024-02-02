from collections import defaultdict

class Solution:
    def largestPalindromic(self, num: str) -> str:
        digitCount = defaultdict(int)
        for char in num:
            digitCount[int(char)] += 1
        reverselySortedDigits = sorted(digitCount.keys())[::-1]

        firstHalf = []
        maxDigitAppearOnce = None
        for digit in reverselySortedDigits:
            for i in range(digitCount[digit] // 2):
                firstHalf.append(str(digit))
            if digitCount[digit] % 2 != 0 and maxDigitAppearOnce is None:
                maxDigitAppearOnce = str(digit)

        if not firstHalf:
            return maxDigitAppearOnce
        if firstHalf[0] == '0':
            return '0' if maxDigitAppearOnce is None else maxDigitAppearOnce

        firstHalfStr = ''.join(firstHalf)
        if maxDigitAppearOnce is not None:
            return firstHalfStr + maxDigitAppearOnce + firstHalfStr[::-1]
        else:
            return firstHalfStr + firstHalfStr[::-1]
