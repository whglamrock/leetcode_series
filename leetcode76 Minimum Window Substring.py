
from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''

        # tCount is used for comparing with sWindow
        tCount = Counter(t)
        # the need & missing are to achieve O(1) time for checking if we have a valid window
        need = Counter(t)
        missing = len(t)

        # left & right index for the ans
        I, J = 0, 0
        # the left index of the s window
        i = 0
        window = defaultdict(int)

        for j, char in enumerate(s):
            # see if we have found 1 more char we are missing
            if char in need and need[char] > 0:
                missing -= 1
                need[char] -= 1

            # track the count of chars in the current window
            window[char] += 1

            # don't do anything unless missing == 0;
                # missing == 0 also makes sure i != j because t is not empty at this point
            if missing == 0:
                while i < j and (s[i] not in tCount or window[s[i]] > tCount[s[i]]):
                    window[s[i]] -= 1
                    i += 1
                if J == 0 or J - I >= j + 1 - i:
                    I, J = i, j + 1

        return s[I:J]



print Solution().minWindow('abbdcecbgaaw', 'abc')
print Solution().minWindow('ADOBECODEBANC', 'ABC')
print Solution().minWindow('ADOBECODEBANC', 'ABCC')