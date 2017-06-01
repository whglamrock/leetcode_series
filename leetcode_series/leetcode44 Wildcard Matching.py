
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

class Solution(object):
    def isMatch(self, s, p):

        if p == None or s == None:
            return False
        if not p:
            return s == ''
        # when all '*'s represents empty sequence, s and p still don't match
        if len(p) - p.count('*') > len(s):
            return False

        lengthofs = len(s)
        # build a one dimensional dp, and after every outer for loop, the whole dp is updated once
        dp = [False] * (lengthofs + 1)
        # means initially, the empty subtring p[:0] matches s[:0]
        dp[0] = True

        # in each loop, we compare the whole s with the partial p until the last loop
        #   the i for loop goes through the s
        for char in p:
            if char != '*':
                for i in xrange(lengthofs - 1, -1, -1):
                    if char == s[i] or char == '?':
                        dp[i + 1] = dp[i]   # dp[i] means whether s[:i] matches the partial p
                    else:
                        dp[i + 1] = False
            else:
                # the '*' can make sure that once some s[:i] matches p[:the index of char],
                #   p[:the index of char + 1] will match the whole s
                for i in xrange(1, lengthofs + 1):  # the i starts from 1 because the '*' can match zero chars
                    # the dp[i] is the dp[i] from previous big for loop,
                    #   and dp[i - 1] is updated in the previous small for loop
                    if dp[i] or dp[i - 1]:
                        # if dp[i] == True, the new dp[i] = True because the '*' can match zero chars
                        # if dp[i - 1] == True, the new dp[i] = True because the '*' can match one more char of s
                        dp[i] = True
                    else:
                        dp[i] = False
            # after the first round of the big for loop, the dp[0] needs to be updated;
            #   and the only way it remains True is p == '*****..', etc.
            dp[0] = dp[0] and char == '*'   # in real interview, don't forget to update



s = "abcd"
p = "a*"
s1 = 'ac'
p1 = 'ac*'
Sol = Solution()

print Sol.isMatch(s, p)
print Sol.isMatch(s1, p1)


