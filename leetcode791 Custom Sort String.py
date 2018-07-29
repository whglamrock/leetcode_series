
from collections import defaultdict

class Solution(object):
    def customSortString(self, S, T):

        ans = []
        letterCount = defaultdict(int)
        for c in T:
            letterCount[c] += 1

        for c in S:
            if c not in letterCount:
                continue
            for i in xrange(letterCount[c]):
                ans.append(c)
            del letterCount[c]

        # deal with the leftover letters
        for c in letterCount:
            for i in xrange(letterCount[c]):
                ans.append(c)

        return ''.join(ans)



print Solution().customSortString("cba", "abcd")
