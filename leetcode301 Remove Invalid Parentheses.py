from typing import List

# Using a visited set to avoid TLE.
# This BFS solution, not optimal but practical to be thought of, is definitely acceptable in real interview.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        visited = set()
        todo = {s}
        while todo:
            nextTodo = set()
            for currStr in todo:
                if ans and len(currStr) < len(ans[0]):
                    return list(set(ans))
                visited.add(currStr)

                if self.isValid(currStr):
                    ans.append(currStr)
                    # there is no need to remove one more parenthesis
                    continue

                for i in range(len(currStr)):
                    if currStr[i] not in '()' or (i > 0 and currStr[i] == currStr[i - 1]):
                        continue
                    nextStr = currStr[:i] + currStr[i + 1:]
                    if nextStr not in visited:
                        visited.add(nextStr)
                        nextTodo.add(nextStr)
            todo = nextTodo

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
                    continue
                return False

        return len(stack) == 0


print(Solution().removeInvalidParentheses("(a)()())"))
print(Solution().removeInvalidParentheses(")()))(e)(()y("))
print(Solution().removeInvalidParentheses(")("))
print(Solution().removeInvalidParentheses("()())()"))
