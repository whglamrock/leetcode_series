from collections import defaultdict
from functools import lru_cache

# you should be able to observe that any possible scramble comes from s1's prefix matching s2's prefix
# or s1's prefix match s2's suffix. Then we need to recursively check the the prefix/substring can be further scrambled.
class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 == s2

        # 2 prefix match
        s1Counter, s2Counter = defaultdict(int), defaultdict(int)
        possibleScramble = False
        for i in range(len(s1) - 1):
            s1Counter[s1[i]] += 1
            s2Counter[s2[i]] += 1
            if s1Counter == s2Counter:
                possibleScramble |= self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:])

        # prefix match suffix:
        s1Counter, s2Counter = defaultdict(int), defaultdict(int)
        for i in range(len(s1) - 1):
            s1Counter[s1[i]] += 1
            s2Counter[s2[len(s2) - i - 1]] += 1
            if s1Counter == s2Counter:
                possibleScramble |= self.isScramble(s1[:i + 1], s2[len(s2) - i - 1:]) \
                                    and self.isScramble(s1[i + 1:], s2[:len(s2) - i - 1])

        return possibleScramble


print(Solution().isScramble('great', 'rgeat'))
print(Solution().isScramble('abcde', 'caebd'))
print(Solution().isScramble("xstjzkfpkggnhjzkpfjoguxvkbuopi", "xbouipkvxugojfpkzjhnggkpfkzjts"))
