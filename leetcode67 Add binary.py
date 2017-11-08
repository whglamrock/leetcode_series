
from collections import deque

class Solution(object):
    def addBinary(self, a, b):

        if len(a) < len(b):
            a, b = b, a

        for i in xrange(len(a) - len(b)):
            b = '0' + b

        carry = 0
        digits = deque()
        for i in xrange(len(a) - 1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                digits.appendleft(str(carry))
                carry = 0
            elif a[i] == '1' and b[i] == '1':
                digits.appendleft(str(carry))
                carry = 1
            else:
                if carry == 1:
                    digits.appendleft('0')
                else:
                    digits.appendleft('1')
        if carry:
            digits.appendleft('1')

        return ''.join(digits)



a = '11'
b = '11'
d = Solution()
c = d.addBinary(a,b)
print c








