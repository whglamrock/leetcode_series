# see discussion for another interesting solution:
# https://discuss.leetcode.com/topic/3040/linear-runtime-and-constant-space-solution
# Essentially it's backtracking, not O(n).

# Also, it's not regular expression, so '*' can match multiple different chars,
# e.g, 'abc' does not match 'a', but matches 'a*'
# consider test case: s = abcdbaef, p = abc*a*e
#                     s = ab, p = *?*c*
#                     s = aaaaaaaaaaaaaaa, p = *aab

# O(p*s) time, O(s) space solution, reduce the dp table to 1D.
# Pay attention the different directions of dp.
# The logic of dealing with '*':
#   1) Divide into two conditions: a) old dp[i] is True; b) old dp[i] is False
#   2) if old dp[i] is True, then the '*' can represent an empty sequence, so new dp[i] = True
#   3) else, see if the p[:char] + '*' (i.e., p[:char + 1]) matches s[:i], if it does, the '*'
#      won't mind "creating another virtual char" to match s[i]. If the updated dp[i - 1] is
#      False, then even if the '*' can match the s[i] by virtually creating one more char,
#      the whole p[:char + 1] won't match s[:i + 1].

class Solution():
    def isMatch(self, s, p):

        length = len(s)
        # even if all '*'s represents empty sequence
        if len(p) - p.count('*') > length:
            return False

        dp = [True] + [False] * length
        # after every outer for loop, the whole dp is updated once
        # the dp[i] means whether p[:char + 1] matches s[:i] (dp's length is longer than s by 1)
        for char in p:
            if char != '*':
                for i in reversed(range(length)):
                    # the dp[i] is the status at i in the previous iteration,
                    # which tells whether s[:i] matches p[:char]
                    dp[i + 1] = dp[i] and (s[i] == char or char == '?')
                    # all new status of dp[i] is based on the previous
                    # status of previous element dp[i - 1].
            else:
                for i in xrange(1, length + 1):
                # if the old dp[i] is True, it means s[:i] matches p[:char]
                # the '*' should represent empty sequence
                    if dp[i] == True or dp[i - 1] == True:  # old dp[i] and updated dp[i - 1]
                        dp[i] = True
                    else:
                        dp[i] = False
                # a simple example when updated dp[i - 1] is False but dp[i] could still be
                # True if old dp[i] is True: 'a' doesn't match 'ac*', but 'ac' matches 'ac*'
                # because 'ac' matches 'ac'.
            # after the first round, the dp[0] needs to be updated;
            # and the only way it remains True is p == '*****..', etc.
            dp[0] = dp[0] and (char == '*')
            #print dp

        return dp[-1]


s = "abcd"
p = "a*"
s1 = 'ac'
p1 = 'ac*'
Sol = Solution()
# print dp in each outer for loop.
print Sol.isMatch(s, p)
print Sol.isMatch(s1, p1)


