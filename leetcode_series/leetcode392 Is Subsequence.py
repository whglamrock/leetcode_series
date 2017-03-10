# O(n) running time solution.
class Solution(object):
    def isSubsequence(self, s, t):

        start = 0
        for i in xrange(len(s)):
            while start < len(t) and t[start] != s[i]:
                start += 1
            if start == len(t):
                return False
            else:
                start += 1    # same character in t can't be used twice (e.g. s='leeeetcode', t='letcode')

        return True