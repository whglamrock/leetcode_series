# The most important for building the dp array: we need to realize the edge case where
# C = B ( A ), then the length of C actually = len(A) + 2 + len(B).
# P.S., for all parentheses problem, it's wrong to simply it into all new valid parenthesis comes from
# previousValid + '()' or '(' + previousValid + ')'.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            currChar = s[i - 1]
            if currChar == '(':
                continue
            prevChar = s[i - 2]
            if prevChar == '(':
                dp[i] = dp[i - 2] + 2
            elif prevChar == ')':
                prevLen = dp[i - 1]
                if prevLen > 0 and i - 1 - prevLen - 1 >= 0 and s[i - 1 - prevLen - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - 1 - prevLen - 1]

        return max(dp)


print(Solution().longestValidParentheses(")()())"))
print(Solution().longestValidParentheses("))()((()()()())"))
