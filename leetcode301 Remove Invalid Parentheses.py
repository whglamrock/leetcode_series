from collections import deque
from typing import List

# Using a visited set to avoid TLE.
# This solution, not optimal but practical to be thought of, should be accepted in real interview.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = deque([s])
        ans = []
        visited = set()
        while queue:
            currStr = queue.popleft()
            visited.add(currStr)
            if self.isValid(currStr):
                if not ans or len(ans[0]) == len(currStr):
                    ans.append(currStr)
            # generate all combinations
            for i in range(len(currStr)):
                if currStr[i] not in '()' or (i > 0 and currStr[i] == currStr[i - 1]):
                    continue
                newStr = currStr[:i] + currStr[i + 1:]
                if newStr not in visited:
                    queue.append(newStr)
                    # pre-add it here instead of checking it when it's popleft'ed from queue to speed up
                    visited.add(newStr)

        return list(set(ans))

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char not in '()':
                continue
            if char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


print(Solution().removeInvalidParentheses("(a)()())"))
print(Solution().removeInvalidParentheses(")()))(e)(()y("))
print(Solution().removeInvalidParentheses(")("))
print(Solution().removeInvalidParentheses("()())()"))
