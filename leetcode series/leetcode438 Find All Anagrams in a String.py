# Sliding window solution. O(n) time, n is the length of s.

from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):

        if len(s) < len(p):
            return []

        pdic = defaultdict(int)
        for letter in p:
            pdic[letter] += 1

        window = defaultdict(int)
        for i in xrange(len(p)):
            window[s[i]] += 1

        ans = []
        if window == pdic:
            ans.append(0)

        i = 1
        while i <= len(s) - len(p):
            leftletter = s[i - 1]
            window[leftletter] -= 1
            if window[leftletter] == 0:
                del window[leftletter]
            newletter = s[i + len(p) - 1]
            window[newletter] += 1
            # because the size of both maps are within 26, comparison takes O(1) time
            if window == pdic:
                ans.append(i)
            i += 1

        return ans

