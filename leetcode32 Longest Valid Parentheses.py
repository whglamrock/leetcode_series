
# the idea is to get out of the idea of "is this string a valid"
# but focus on if we have any substring

# P.S. it's hard to know we should keep a stack to store the unmatched
# indices, but it's the key to solution

class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0

        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            i += 1

        if not stack:  # the whole string is valid
            return len(s)
        else:
            longest = max(stack[0], len(s) - 1 - stack[-1])
            for j in xrange(len(stack) - 1):
                longest = max(longest, stack[j + 1] - stack[j] - 1)
            return longest



Sol = Solution()
print Sol.longestValidParentheses(")()())")
print Sol.longestValidParentheses("))()((()()()())")