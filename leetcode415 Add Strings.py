
from collections import deque

class Solution(object):
    def addStrings(self, num1, num2):

        res = deque()
        trans = 0
        i = 0
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]
        n = len(num1)
        while i < n:
            digit = (int(num1[i]) + int(num2[i]) + trans) % 10
            res.appendleft(str(digit))
            trans = (int(num1[i]) + int(num2[i]) + trans) / 10
            i += 1

        while n < len(num2):
            digit = (int(num2[n]) + trans) % 10
            res.appendleft(str(digit))
            trans = (int(num2[n]) + trans) / 10
            n += 1

        if trans: res.appendleft(str(trans))
        return ''.join(res)