
# KMP can get O(M + N) but it's not really necessary in real interview.
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        for char in s:
            stack.append(char)
            while len(stack) >= m and ''.join(stack[len(stack) - m:]) == part:
                for i in range(m):
                    stack.pop()

        return ''.join(stack)
