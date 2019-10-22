
# RPN definition: https://en.wikipedia.org/wiki/Reverse_Polish_notation

class Solution(object):
    def evalRPN(self, tokens):

        operands = '+-*/'
        stack = []
        i = 0

        while i < len(tokens):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(num1 + num2)
                elif tokens[i] == '-':
                    stack.append(num1 - num2)
                elif tokens[i] == '*':
                    stack.append(num1 * num2)
                else:
                    flag = 1
                    if (num1 * num2) < 0:
                        flag = -1
                    num1, num2 = abs(num1), abs(num2)
                    stack.append(flag * (num1 / num2))    # for stupid test case like 6/(-132).
                    # in python, it returns -1. but in java, it returns 0.
            i += 1

        return stack.pop()



print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
