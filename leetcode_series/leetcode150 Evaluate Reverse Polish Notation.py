# https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95
# see the definition of reverse polish notation above.
class Solution(object):
    def evalRPN(self, tokens):

        operators = set(['+','-','*','/'])
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(num1+num2)
                elif tokens[i] == '-':
                    stack.append(num1-num2)
                elif tokens[i] == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(int(float(num1)/num2))    # for stupid test case like 6/(-132).
                    # in python, it returns -1. but in java, it returns 0.
            i += 1

        if (not stack):
            return
        else:
            return stack.pop()


Sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print Sol.evalRPN(tokens)
