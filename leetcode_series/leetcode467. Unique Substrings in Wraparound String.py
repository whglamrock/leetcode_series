
from collections import defaultdict
class Solution(object):
    def findSubstringInWraproundString(self, p):

        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        cmap = defaultdict(int)
        # records the start and end of the current substring
        start = end = 0

        for i in xrange(len(p)):
            # means the consecutive substring ends
            if i > 0 and p[i - 1:i + 1] not in pattern:
                for j in xrange(start, end):
                    cmap[p[j]] = max(end - j, cmap[p[j]])
                start = i
            end = i + 1

        # the following for loop does the job of above if statement for the last time
        for j in xrange(start, end):
            cmap[p[j]] = max(end - j, cmap[p[j]])

        # e.g., p = 'abcd', then cmap = {a: 4, b: 3, c: 2, d: 1}
        # IMPORTANT: summing them up == looking at them as (a, b, c, d, ab, bc, cd, abc, bcd, abcd)
        return sum(cmap.values())