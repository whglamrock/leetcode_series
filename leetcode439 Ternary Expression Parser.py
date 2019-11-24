
# the hard part is to think of scanning the expression from right to left

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        if not expression:
            return ''

        stack = []
        for char in expression[::-1]:
            if stack and stack[-1] == '?':
                # pop the '?'
                stack.pop()
                # it's guaranteed that each number only has 1 char
                firstChar = stack.pop()
                # pop the ':'
                stack.pop()
                secondChar = stack.pop()

                if char == 'T':
                    stack.append(firstChar)
                else:
                    stack.append(secondChar)
            else:
                stack.append(char)

        return stack[0]



print Solution().parseTernary('F?1:T?6:5')
print Solution().parseTernary('T?T?F:5:3')
print Solution().parseTernary('8')