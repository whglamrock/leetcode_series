
from collections import defaultdict

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if not A:
            return []

        valToIndex = defaultdict(list)
        for i, val in enumerate(B):
            valToIndex[val].append(i)

        ans = [-1] * len(A)
        for i, val in enumerate(A):
            ans[i] = valToIndex[val].pop()

        return ans
