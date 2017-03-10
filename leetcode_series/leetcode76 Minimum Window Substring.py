# remember the idea of 'missing' and 'need'
# edge case: t doesn't exist in s

from collections import Counter
class Solution(object):
    def minWindow(self, s, t):

        if t == None or s == None:
            return
        if not t or not s:
            return ''
        if len(s) < len(t):
            return ''

        need, missing = Counter(t), len(t)
        # i,j is the start/end index of current valid window
        i = 0
        # big convenience to do this:
        I = J = 0
        #tset = set(t)

        # need[c] < 0 means we don't need this char
        for j, char in enumerate(s):

            # is c not in need, need will automatically initialize need[c] = 0,
            #   Counter is a subclass of defaultdict type
            if need[char] > 0:  # the condition needs to be need[char] > 0, instead of "char in tset"
                missing -= 1
            need[char] -= 1

            # missing == 0 means we found a valid window and we are gonna shrink it
            if missing == 0:
                # need[s[i]] < 0 means we don't need this char
                #   and if the char is in t, need[t] will always >= 0
                while i <= j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                # J == 0 is the initial status, if J remains 0, then the missing never == 0,
                #   which means the t is not in the s;
                # j is the end index of window so the length = j - i + 1
                if J == 0 or (j + 1) - i <= J - I:
                    I, J = i, j + 1

        # Initializing I = J = 0 also fits the condition that t doesn't exist in s
        return s[I:J]



Sol = Solution()
s = 'abdcewgaw'
t = 'abc'
print Sol.minWindow(s, t)
