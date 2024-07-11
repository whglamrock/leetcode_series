from math import floor
from typing import List


# If the followup question requires O(1) space, it became a hard level question. Remember the O(1) space solution at
# the bottom.
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


'''
# O(1) space solution coming from: https://www.geeksforgeeks.org/evaluate-the-value-of-an-arithmetic-expression-in-reverse-polish-notation-in-java/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lastNumIndex = -1
        i = 0
        while i < len(tokens):
            if tokens[i] in '+-*/':
                num2 = tokens[lastNumIndex]
                num1 = tokens[lastNumIndex - 1]
                if tokens[i] == '+':
                    result = num1 + num2
                elif tokens[i] == '-':
                    result = num1 - num2
                elif tokens[i] == '*':
                    result = num1 * num2
                else:
                    if num1 * num2 >= 0:
                        result = num1 // num2
                    else:
                        result = -(abs(num1) // abs(num2))
                
                tokens[lastNumIndex - 1] = result
                lastNumIndex -= 1
            else:
                lastNumIndex += 1
                tokens[lastNumIndex] = int(tokens[i])
            
            i += 1
        
        return tokens[lastNumIndex]
'''