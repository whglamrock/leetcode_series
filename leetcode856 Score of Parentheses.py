
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    currScore = 0
                    while type(stack[-1]) == int:
                        currScore += stack.pop()
                    stack.pop()
                    stack.append(currScore * 2)

        return sum(stack)