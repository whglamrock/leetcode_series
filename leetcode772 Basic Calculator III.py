class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        sign = '+'
        while i < len(s):
            if s[i].isdigit():
                curr = 0
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                if stack and stack[-1] == '*':
                    stack.pop()
                    prevNum = stack.pop()
                    stack.append(prevNum * curr)
                elif stack and stack[-1] == '/':
                    stack.pop()
                    prevNum = stack.pop()
                    # a '/' won't be followed by a non-negative number (i.e., curr > 0)
                    # so we only need to check the sign of the previous number
                    if prevNum > 0:
                        stack.append(prevNum // curr)
                    else:
                        prevNum = -prevNum
                        stack.append(-(prevNum // curr))
                else:
                    if sign == '+':
                        stack.append(curr)
                    else:
                        stack.append(-curr)
            elif s[i] == '+':
                sign = '+'
                i += 1
            elif s[i] == '-':
                sign = '-'
                i += 1
            # reset the sign because '*/' must be followed by a non-negative number
            elif s[i] in '*/':
                sign = '+'
                stack.append(s[i])
                i += 1
            elif s[i] == '(':
                if sign == '+':
                    stack.append('(')
                else:
                    stack.append('-(')
                sign = '+'
                i += 1
            else:
                chunkSum = 0
                while stack[-1] not in ['(', '-(']:
                    chunkSum += stack.pop()
                openParenthesis = stack.pop()
                if openParenthesis == '-(':
                    chunkSum = -chunkSum

                if stack and stack[-1] == '*':
                    stack.pop()
                    prevNum = stack.pop()
                    stack.append(chunkSum * prevNum)
                elif stack and stack[-1] == '/':
                    stack.pop()
                    prevNum = stack.pop()
                    if prevNum * chunkSum < 0:
                        stack.append(-(abs(prevNum) // abs(chunkSum)))
                    else:
                        stack.append(prevNum // chunkSum)
                else:
                    stack.append(chunkSum)
                i += 1

        return sum(stack)


print(Solution().calculate("2*(5+5*2)/3-3/(6/2-8/4)"))
print(Solution().calculate("5-3/2"))
print(Solution().calculate("3/(2/1-4)"))
