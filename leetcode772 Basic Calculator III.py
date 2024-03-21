class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        n = len(s)
        sign = '+'
        while i < n:
            if s[i].isdigit():
                curr = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    curr = curr * 10 + int(s[i + 1])
                    i += 1
                # in this case curr must be a positive number
                if stack and (type(stack[-1]) == str and stack[-1] in '*/'):
                    operand = stack.pop()
                    prevNum = stack.pop()
                    if operand == '*':
                        stack.append(prevNum * curr)
                    else:
                        if prevNum < 0:
                            stack.append(-(-prevNum // curr))
                        else:
                            stack.append(prevNum // curr)
                elif sign == '+':
                    stack.append(curr)
                else:
                    stack.append(-curr)
                    sign = '+'
            elif s[i] in '+-':
                sign = s[i]
            elif s[i] in '*/':
                stack.append(s[i])
            elif s[i] == '(':
                if sign == '+':
                    stack.append('(')
                else:
                    stack.append('-(')
                    # always reset the sign when we add anything to the stack
                    sign = '+'
            # s[i] == ')', need to pop
            else:
                curr = stack.pop()
                while not (type(stack[-1]) == str and stack[-1] in ['-(', '(']):
                    curr += stack.pop()
                openParenthesisToken = stack.pop()
                # in this case the current stack[-1] won't be '*/'
                if openParenthesisToken == '-(':
                    stack.append(-curr)
                else:
                    if stack and (type(stack[-1]) == str and stack[-1] in '*/'):
                        if stack[-1] == '*':
                            stack.pop()
                            prevNum = stack.pop()
                            stack.append(prevNum * curr)
                        else:
                            stack.pop()
                            prevNum = stack.pop()
                            if prevNum * curr < 0:
                                stack.append(-(abs(prevNum) // abs(curr)))
                            else:
                                stack.append(prevNum // curr)
                    else:
                        stack.append(curr)
            i += 1

        return sum(stack)


print(Solution().calculate("2*(5+5*2)/3-3/(6/2-8/4)"))
print(Solution().calculate("5-3/2"))
print(Solution().calculate("3/(2/1-4)"))
