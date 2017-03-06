
from collections import deque
class Solution(object):

    def addBinary(self, a, b):

        if len(a) < len(b):
            a, b = b, a

        barray = deque(char for char in b)
        for i in xrange(len(b), len(a)):
            barray.appendleft('0')
        b = ''.join(barray)

        ans = deque()
        carry = '0'
        for i in xrange(len(a) - 1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                ans.appendleft(carry)
                carry = '1'
            elif a[i] == '0' and b[i] == '0':
                ans.appendleft(carry)
                carry = '0'
            else:
                if carry == '1':
                    ans.appendleft('0')
                else:
                    ans.appendleft('1')
        if carry == '1':
            ans.appendleft('1')

        return ''.join(ans)


a = '11'
b = '11'
d = Solution()
c = d.addBinary(a,b)
print c








