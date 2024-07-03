from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            return -1

        peopleWhoTrustsSomeone = set()
        peopleToTrustedBy = defaultdict(int)
        for a, b in trust:
            peopleWhoTrustsSomeone.add(a)
            peopleToTrustedBy[b] += 1

        numOfJudge = 0
        ans = -1
        for i in range(1, n + 1):
            if i not in peopleWhoTrustsSomeone and i in peopleToTrustedBy and peopleToTrustedBy[i] == n - 1:
                numOfJudge += 1
                ans = i

        return ans if numOfJudge == 1 else -1
