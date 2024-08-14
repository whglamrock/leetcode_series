from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                # we need to use do below instead of appending tokens in reverse order and simply add ''.join(tokens)
                # to stack. This is to avoid wrong answers for case like "a(bcdefghijkl(mno)p)q"
                tokens = deque()
                while stack[-1] != '(':
                    tokens.appendleft(stack.pop())
                stack.pop()
                stack.append(''.join(tokens)[::-1])
            else:
                stack.append(s[i])
            i += 1

        return ''.join(stack)
