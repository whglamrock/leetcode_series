class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        stack = []
        operator = None
        for i, char in enumerate(s):
            if char == ' ':
                continue
            if char in '+-*/':
                operator = char
            else:
                curr = curr * 10 + int(char)
                # need to add number to stack
                if i + 1 >= len(s) or not s[i + 1].isdigit():
                    if operator == '+' or operator is None:
                        stack.append(curr)
                    elif operator == '-':
                        stack.append(-curr)
                    elif operator == '*':
                        prevNum = stack.pop()
                        stack.append(prevNum * curr)
                    else:
                        prevNum = stack.pop()
                        isNegative = prevNum < 0
                        curr = abs(prevNum) // curr
                        if isNegative:
                            curr = -curr
                        stack.append(curr)
                    curr = 0

        return sum(stack)


print(Solution().calculate("3 + 2 * 2"))
print(Solution().calculate("4 + 2 * 2 - 4 / 3 + 3 / 1 * 2 / 1"))
print(Solution().calculate("3 + 2 * 2- 18 - 29 / 3"))
