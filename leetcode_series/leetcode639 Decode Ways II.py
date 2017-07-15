
class Solution(object):
    def numDecodings(self, s):

        # no need to check whether s is None or an empty string based on the problem definition
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        bignumber = 10 ** 9 + 7  # stupid overflow

        for i in xrange(1, n + 1):
            # treat s[i - 1] as a single char
            if s[i - 1] == '*':
                dp[i] += dp[i - 1] * 9
            elif s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # treat s[i - 2:i] as a substring of two letters
            if i >= 2 and s[i - 2] == '1':
                if s[i - 1].isdigit():
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += dp[i - 2] * 9
            if i >= 2 and s[i - 2] == '2':
                if '0' <= s[i - 1] <= '6':
                    dp[i] += dp[i - 2]
                elif s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 6
            if i >= 2 and s[i - 2] == '*':
                if s[i - 1].isdigit():
                    dp[i] += dp[i - 2]  # consider s[i - 2] as '1'
                    if '0' <= s[i - 1] <= '6':
                        dp[i] += dp[i - 2]  # consider s[i - 2] as '1'
                else:
                    dp[i] += dp[i - 2] * 15  # '**' can't be 1~9, or 10, 20
            dp[i] = (dp[i] + bignumber) % bignumber

        return dp[-1]



Sol = Solution()
s = '***'
print Sol.numDecodings(s)
