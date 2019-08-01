
from collections import deque

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = deque()
        for char in s:
            q.append(char)
        # this is to trigger the "stack.append(num)" to avoid dropping the last number
        q.append('+')
        return self.cal(q)

    def cal(self, q):
        # set default sign for the "first" number
        sign = '+'
        num = 0
        stack = []
        while q:
            c = q.popleft()
            if c == ' ':
                continue
            # in this case num is definitely 0
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '(':
                num = self.cal(q)
            # only add the number to stack when it's sign or ')'
            else:
                # the sign is the previous sign
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    lastNum = stack.pop()
                    # in python -3 / 2 = -2 instead of -1
                    if lastNum < 0:
                        lastNum = -lastNum
                        stack.append(-(lastNum / num))
                    else:
                        stack.append(lastNum / num)
                # means we are already in recursion, needs to return the result of this block instead of further popleft q
                if c == ')':
                    break
                num = 0
                sign = c

        return sum(stack)



print Solution().calculate(s="6-3 / 2")
print Solution().calculate(s="(2+6* 3+5- (3*14/7+2)*5)+3")





