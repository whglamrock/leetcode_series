
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
        return self.cal(q)

    def cal(self, q):
        sign = '+'
        num = 0
        stack = []
        while q:
            c = q.popleft()
            if c == '(':
                num = self.cal(q)
            elif c.isdigit():
                num = num * 10 + int(c)
            # this is when we need to add the num to stack
            else:
                # the sign records the previous sign
                if sign == '+':
                    stack.append(num)
                else:
                    stack.append(-num)
                    # break to return the sum(stack) as the result of this sub
                    # expression within a parenthesis pair
                if c == ')':
                    break
                num = 0
                sign = c

        return sum(stack)



sol = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
print sol.calculate(s)





