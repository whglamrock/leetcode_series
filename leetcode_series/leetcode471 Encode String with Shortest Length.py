
# remember the dp idea

class Solution(object):
    def encode(self, s):

        n = len(s)
        dp = [['' for j in xrange(n)] for i in xrange(n)]

        # l is the length of the substring (but l could be as most n - 1 so we need adjustments)
        for l in xrange(n):
            # i the start index of substring
            for i in xrange(n - l):
                # j is end index, so we use j + 1 for the slicing
                j = i + l
                substr = s[i: j + 1]

                # the orignal substring is shorter than the encoded form
                if l < 4:
                    dp[i][j] = substr
                else:
                    dp[i][j] = substr
                    # the first loop check is we can add encoded forms of two substrings
                    #   of substr to make dp[i][j] shorter
                    for k in xrange(i, j):
                        if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k + 1][j]

                    # the second loop check if we can repeated pattern for substr
                    # k is the length of repeatedstr
                    for k in xrange(len(substr) / 2):
                        repeatedstr = substr[:k + 1]
                        if len(substr) % len(repeatedstr) == 0 and len(substr.replace(repeatedstr, '')) == 0:
                            ss = str(len(substr) / len(repeatedstr)) + '[' + dp[i][i + k] + ']'
                            if len(ss) < len(dp[i][j]): dp[i][j] = ss

        return dp[0][-1]

