class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        n = len(s)
        operand = '+'
        while i < n:
            if s[i] == '-':
                operand = '-'
            elif s[i] == '+':
                operand = '+'
            elif s[i].isdigit():
                num = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                if operand == '-':
                    stack.append(-num)
                else:
                    stack.append(num)
            elif s[i] == '(':
                if operand == '+':
                    stack.append('(')
                else:
                    stack.append('-(')
                operand = '+'
            elif s[i] == ')':
                sumOfChunk = 0
                while stack[-1] not in ['(', '-(']:
                    sumOfChunk += stack.pop()
                if stack[-1] == '-(':
                    stack.pop()
                    stack.append(-sumOfChunk)
                else:
                    stack.pop()
                    stack.append(sumOfChunk)

            # ignore when s[i] == ' '
            i += 1

        return sum(stack)


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("(1-(-4+5+2)-3)+(6+8)"))
