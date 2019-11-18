
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        stack = []
        num = []

        for c in s:
            if c.isdigit():
                num.append(c)
            elif c == '[':
                stack.append(int(''.join(num)))
                num = []
                stack.append(c)
            elif c == ']':
                charArray = []
                while stack and stack[-1] != '[':
                    charArray.append(stack.pop())
                charChunk = ''.join(charArray[::-1])

                # pop the '['
                stack.pop()

                lastNum = stack.pop()
                flattenedStr = []
                for i in xrange(lastNum):
                    flattenedStr.append(charChunk)
                stack.append(''.join(flattenedStr))
            else:
                stack.append(c)

        return ''.join(stack)



print Solution().decodeString('3[a2[c]]ef')
print Solution().decodeString('3[a]2[bc]')
print Solution().decodeString('2[abc]3[cd]ef')




