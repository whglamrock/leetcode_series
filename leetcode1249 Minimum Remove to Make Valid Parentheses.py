
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char not in '()':
                continue
            if char == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

        invalidIndexes = set(stack)
        ans = []
        for i, char in enumerate(s):
            if i not in invalidIndexes:
                ans.append(char)

        return ''.join(ans)


sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
print(sol.minRemoveToMakeValid("a)b(c)d"))
print(sol.minRemoveToMakeValid("))(("))
