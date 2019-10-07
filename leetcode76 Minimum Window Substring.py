
# remember the idea of 'missing' and 'need'
# edge case: t doesn't exist in s

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):

        if not s or not t:
            return ''

        i = 0
        I = J = 0
        need, missing = Counter(t), len(t)

        # valid window = s[i:j + 1])
        for j, char in enumerate(s):

            # the need dict just tracks what we need/miss; need[char] > 0 only possible for char in t
            if need[char] > 0:
                # once miss reached 0, we don't increase it any more. i.e., the window stays valid
                missing -= 1

            # any char with need[char] < 0 is a redundant char
            need[char] -= 1

            # window is valid at this point
            if missing == 0:
                # the first condition -- "i < j" is enough, because the "t is empty" scenario has been ruled out
                #   i <= j is also okay, though
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                if J == 0 or (j + 1) - i < J - I:
                    # note that we set J = j + 1 here to ease dealing with corner case where t not in s
                    J, I = j + 1, i

        # covers the corner case where t not in s
        return s[I:J]



print Solution().minWindow('abbdcecbgaaw', 'abc')
print Solution().minWindow('ADOBECODEBANC', 'ABC')
print Solution().minWindow('ADOBECODEBANC', 'ABCC')