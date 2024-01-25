from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                currDigit = 0
                while i < len(s) and s[i].isdigit():
                    currDigit = currDigit * 10 + int(s[i])
                    i += 1
                stack.append(currDigit)
            elif s[i] == '[':
                i += 1
            elif s[i] == ']':
                currStr = deque()
                # P.S. in case like 3[a2[c]], there might be multiple  consecutive substrings
                # so we need to pop all of them before checking if stack[-1] is an int
                while stack and type(stack[-1]) == str:
                    currStr.appendleft(stack.pop())
                currStr = ''.join(currStr)
                if stack and type(stack[-1]) == int:
                    currStr *= stack.pop()
                stack.append(currStr)
                i += 1
            else:
                stack.append(s[i])
                i += 1

        return ''.join(stack)


print(Solution().decodeString('3[a2[c]]ef'))
print(Solution().decodeString('3[a]2[bc]'))
print(Solution().decodeString('2[abc]3[cd]ef'))
