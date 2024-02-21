# A naive O(N ^ 2) solution gets TLE in the stupid leetcode but should be acceptable in real interview (unless any
# motherfucking stupid interviewer asks for O(M * N) DP solution).
# Below solution optimize the start index but in worst case scenario is still O(N ^ 2) time.
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        minWindowLen = 2147483647
        ans = ''
        i = 0
        while i < len(s1):
            endIndexSuperSeqns = self.findEndIndexOfSuperSeqns(s1, s2, i)
            # break here instead of continue
            if endIndexSuperSeqns == -1:
                break

            bestStartIndexSuperSeqns = self.findStartIndexOfSuperSeqns(s1, s2, i, endIndexSuperSeqns)
            if endIndexSuperSeqns - bestStartIndexSuperSeqns + 1 < minWindowLen:
                minWindowLen = endIndexSuperSeqns - bestStartIndexSuperSeqns + 1
                ans = s1[bestStartIndexSuperSeqns:endIndexSuperSeqns + 1]
            i = bestStartIndexSuperSeqns + 1

        return ans

    def findStartIndexOfSuperSeqns(self, s1: str, s2: str, start: int, end: int) -> int:
        i, j = end, len(s2) - 1
        while i >= start and j >= 0:
            if s1[i] == s2[j]:
                i -= 1
                j -= 1
            else:
                i -= 1

        return i + 1 if j == -1 else start

    def findEndIndexOfSuperSeqns(self, s1: str, s2: str, start: int) -> int:
        i, j = start, 0
        m, n = len(s1), len(s2)
        while i < m and j < n:
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                i += 1

        return i - 1 if j == n else -1
