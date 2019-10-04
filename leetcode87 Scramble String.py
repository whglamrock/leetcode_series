
from collections import defaultdict

# A really boring and meaningless question.
# The only point of this question is to test whether we can think of the divide & conquer idea, then it's natural to
    # write out the recursive solution

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        letterCount1, letterCount2 = defaultdict(int), defaultdict(int)
        n = len(s1)
        if n != len(s2):
            return False

        for i in xrange(n):
            letterCount1[s1[i]] += 1
            letterCount2[s2[i]] += 1
        # guaranteed the s1/s2 only contains lowercase letters
        for letter in s1:
            if letterCount1[letter] != letterCount2[letter]:
                return False

        for i in xrange(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[n - i:n]) and self.isScramble(s1[i:], s2[:n - i]):
                return True

        return False



print Solution().isScramble('great', 'rgeat')
print Solution().isScramble('abcde', 'caebd')







