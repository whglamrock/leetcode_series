from math import floor
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    divisionResult = num1 / num2
                    if divisionResult < 0:
                        divisionResult = -floor(abs(divisionResult))
                    else:
                        divisionResult = floor(divisionResult)
                    stack.append(divisionResult)
            else:
                stack.append(int(token))

        return stack[0]


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
