
from collections import deque

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        q = deque()
        for c in s:
            if c != ' ':
                q.append(c)
        q.append('+')

        stack = []
        num = 0
        sign = '+'
        while q:
            c = q.popleft()
            if c.isdigit():
                num = num * 10 + int(c)
            # we need to calculation at this point
            else:
                # sign records the last sign
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    lastNum = stack.pop()
                    if lastNum < 0:
                        lastNum = -lastNum
                        stack.append(-(lastNum / num))
                    else:
                        stack.append(lastNum / num)

                sign = c
                num = 0

        return sum(stack)



print Solution().calculate(s="3 + 2* 2")