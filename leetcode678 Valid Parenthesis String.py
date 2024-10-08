# Idea:
# 1) Ignore all the *'s. Pick out the invalid parenthesis and save their indexes
# 2) Scan through the s, for invalid parenthesis index, see if there's a * before or after to pair with
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starCount = 0
        for i, char in enumerate(s):
            if char == '*':
                starCount += 1
                continue
            if char == '(':
                stack.append([i, char])
            else:
                if stack and stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append([i, char])

        if not stack:
            return True
        if len(stack) > starCount:
            return False

        invalidIndexes = set()
        for i, char in stack:
            invalidIndexes.add(i)

        stack = []
        for i, char in enumerate(s):
            if char == '*':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
            elif i not in invalidIndexes:
                continue
            # invalid '(' or ')'
            else:
                if char == ')' and stack and stack[-1] == '*':
                    stack.pop()
                else:
                    stack.append(char)

        for char in stack:
            if char != '*':
                return False
        return True
