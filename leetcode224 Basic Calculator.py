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
                if sign == '+':
                    stack.append(curr)
                else:
                    stack.append(-curr)
                    sign = '+'
            elif s[i] in '+-':
                sign = s[i]
            elif s[i] == '(':
                if sign == '+':
                    stack.append('(')
                else:
                    stack.append('-(')
                    sign = '+'
            # s[i] == ')'
            else:
                # need to pop
                curr = stack.pop()
                while not (type(stack[-1]) == str and stack[-1] in ['-(', '(']):
                    curr += stack.pop()
                openParenthesisToken = stack.pop()
                if openParenthesisToken == '-(':
                    stack.append(-curr)
                else:
                    stack.append(curr)
            i += 1

        return sum(stack)


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution().calculate("(1-(-4+5+2)-3)+(6+8)"))
