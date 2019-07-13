
from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        minCount = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            minCount[c] = 2147483647

        for s in A:
            sCount = Counter(s)
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c not in sCount:
                    sCount[c] = 0
                minCount[c] = min(minCount[c], sCount[c])

        ans = []
        for c in minCount:
            for i in xrange(minCount[c]):
                ans.append(c)

        return ans



print Solution().commonChars(A = ["bella","label","roller"])
