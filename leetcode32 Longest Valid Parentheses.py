
# non stack dp solution is easier to think of in real interview

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        for i in xrange(1, n + 1):
            if s[i - 1] == '(':
                continue
            # previous char is '('
            if i >= 2 and s[i - 2] == '(':
                dp[i] = dp[i - 2] + 2
            # previous char is ')', then we need to check the longest length before previous ')' 's corresponding '('.
            elif i >= 2 and s[i - 2] == ')' and dp[i - 1]:
                prevLen = dp[i - 1]
                # let the longest valid parentheses the ends with s[i - 2] be A, so the longest streak that ends
                    # with s[i - 1] must something like '( A )'. It's impossible that a single ')' along with
                    # part of A can form a valid streak.
                # Thus, the longest valid streak ends with s[i - 1] is either 0, or len(A) + 2 + len(B), considering
                    # the s = 'xxx B ( A )' where B is longest valid streak that ends right before the '('
                if i - prevLen - 2 >= 0 and s[i - prevLen - 2] == '(':
                    # the 2 is for s[i - 1] and matching '(', also don't forget about dp[i - prevLen - 2]
                    dp[i] = dp[i - 1] + dp[i - prevLen - 2] + 2

        return max(dp)



Sol = Solution()
print Sol.longestValidParentheses(")()())")
print Sol.longestValidParentheses("))()((()()()())")