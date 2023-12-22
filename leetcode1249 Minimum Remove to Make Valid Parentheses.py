class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        invalidIndexes = set()
        for i, char in enumerate(s):
            if char not in '()':
                continue
            if char == '(':
                stack.append([i, '('])
            else:
                if stack and stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append([i, ')'])

        for i, char in stack:
            invalidIndexes.add(i)

        ans = []
        for i, char in enumerate(s):
            if i not in invalidIndexes:
                ans.append(char)

        return ''.join(ans)


sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
print(sol.minRemoveToMakeValid("a)b(c)d"))
print(sol.minRemoveToMakeValid("))(("))
