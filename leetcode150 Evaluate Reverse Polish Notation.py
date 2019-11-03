
# RPN definition: https://en.wikipedia.org/wiki/Reverse_Polish_notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = '+-*/'
        stack = []

        for token in tokens:
            if token in operands:
                # pay attention to the order of assigning num1 & num2, it matters for division
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    # important! remember to check corner case like: 6 / (-132)
                    # in python, it returns -1. but in java, it returns 0.
                    sign = 1
                    if num1 * num2 < 0:
                        sign = -1
                    num1, num2 = abs(num1), abs(num2)
                    stack.append(sign * (num1 / num2))
            else:
                stack.append(int(token))

        return stack[0]



print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
