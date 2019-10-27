
from collections import Counter

# if interviewer asks for one pass solution, use OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        letterCount = Counter(s)
        for i in xrange(len(s)):
            if letterCount[s[i]] == 1:
                return i

        return -1