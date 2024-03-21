class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        sign = '+'
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit():
                curr = int(s[i])
                while i + 1 < len(s) and s[i + 1].isdigit():
                    curr = curr * 10 + int(s[i + 1])
                    i += 1
                if stack and type(stack[-1]) == str and stack[-1] in '*/':
                    operand = stack.pop()
                    lastNum = stack.pop()
                    if operand == '*':
                        stack.append(curr * lastNum)
                    else:
                        if lastNum < 0:
                            stack.append(-(-lastNum // curr))
                        else:
                            stack.append(lastNum // curr)
                else:
                    if sign == '+':
                        stack.append(curr)
                    else:
                        stack.append(-curr)
                        sign = '+'
            elif s[i] in '+-':
                sign = s[i]
            # s[i] == * or /
            else:
                stack.append(s[i])
            i += 1

        return sum(stack)


print(Solution().calculate("3 + 2 * 2"))
print(Solution().calculate("4 + 2 * 2 - 4 / 3 + 3 / 1 * 2 / 1"))
print(Solution().calculate("3 + 2 * 2- 18 - 29 / 3"))
