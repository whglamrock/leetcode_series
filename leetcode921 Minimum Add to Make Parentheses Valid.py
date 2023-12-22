
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack)
