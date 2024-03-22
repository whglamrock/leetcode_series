class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue
            stack.append(char)

        return ''.join(stack)


print(Solution().removeDuplicates('abccbawfd'))
