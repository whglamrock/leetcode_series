
# The question says "You must not use any built-in BigInteger library or convert the inputs to integer directly",
# so we need to use the ord() function which gets the ascii number. Also, if the interviewer is not OK with below
# solution, use the solution at the bottom instead.
class Solution(object):
    def addStrings(self, num1: str, num2: str) -> str:
        int1 = 0
        for char in num1:
            int1 = int1 * 10 + ord(char) - ord('0')

        int2 = 0
        for char in num2:
            int2 = int2 * 10 + ord(char) - ord('0')

        return str(int1 + int2)


'''
from collections import deque

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        ans = deque()
        i, j = m - 1, n - 1
        carry = 0
        while i >= 0 and j >= 0:
            digit1, digit2 = num1[i], num2[j]
            digitSum = (ord(digit1) - ord('0')) + (ord(digit2) - ord('0'))
            digitSum += carry
            if digitSum >= 10:
                carry = 1
            else:
                carry = 0
            ans.appendleft(str(digitSum % 10))
            i -= 1
            j -= 1
        
        while i >= 0:
            digit1 = int(num1[i]) + carry
            if digit1 >= 10:
                carry = 1
            else:
                carry = 0
            ans.appendleft(str(digit1 % 10))
            i -= 1
        
        while j >= 0:
            digit2 = int(num2[j]) + carry
            if digit2 >= 10:
                carry = 1
            else:
                carry = 0
            ans.appendleft(str(digit2 % 10))
            j -= 1
        
        if carry == 1:
            ans.appendleft('1')
        
        return ''.join(ans)
'''