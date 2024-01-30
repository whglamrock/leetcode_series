from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.tens = {}
        self.tenToTwenty = {}
        self.lessThan10 = {}

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        self.lessThan10 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                           9: 'Nine'}
        self.tenToTwenty = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                            16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        self.tens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                     90: 'Ninety'}

        digits = deque()
        while num:
            digits.appendleft(num % 10)
            num //= 10

        englishWords = deque()
        # get the first three digits
        first3Digits = deque()
        for i in range(min(3, len(digits))):
            first3Digits.appendleft(digits.pop())
        if first3Digits:
            first3DigitStr = self.generateEnglishWordsFor3Digits(first3Digits)
            if first3DigitStr:
                englishWords.appendleft(first3DigitStr)
        # get the 2nd three digits
        if digits:
            second3Digits = deque()
            for i in range(min(3, len(digits))):
                second3Digits.appendleft(digits.pop())
            if second3Digits:
                second3DigitStr = self.generateEnglishWordsFor3Digits(second3Digits)
                if second3DigitStr:
                    englishWords.appendleft(second3DigitStr + ' Thousand')
        if digits:
            third3Digits = deque()
            for i in range(min(3, len(digits))):
                third3Digits.appendleft(digits.pop())
            if third3Digits:
                third3DigitStr = self.generateEnglishWordsFor3Digits(third3Digits)
                if third3DigitStr:
                    englishWords.appendleft(third3DigitStr + ' Million')
        if digits:
            forth3Digits = deque()
            for i in range(min(3, len(digits))):
                forth3Digits.appendleft(digits.pop())
            if forth3Digits:
                englishWords.appendleft(self.generateEnglishWordsFor3Digits(forth3Digits) + ' Billion')

        return ' '.join(englishWords).strip()

    def generateEnglishWordsFor3Digits(self, digits: List[int]) -> str:
        englishWords = []
        if len(digits) == 3:
            if digits[0] == 0:
                digits.popleft()
            else:
                englishWords.append(self.lessThan10[digits.popleft()] + ' Hundred')
        if len(digits) == 2:
            if digits[0] == 0:
                digits.popleft()
            elif digits[0] == 1:
                englishWords.append(self.tenToTwenty[digits[0] * 10 + digits[1]])
                digits = []
            else:
                englishWords.append(self.tens[digits.popleft() * 10])
        if len(digits) == 1:
            if digits[0] == 0:
                digits.popleft()
            else:
                englishWords.append(self.lessThan10[digits.popleft()])

        if not englishWords:
            return ''
        return ' '.join(englishWords).strip()


print(Solution().numberToWords(1000000))
print(Solution().numberToWords(401002))
print(Solution().numberToWords(2147480040))
print(Solution().numberToWords(2147483647))
print(Solution().numberToWords(0))
print(Solution().numberToWords(123))
print(Solution().numberToWords(1234))
print(Solution().numberToWords(1234567))
