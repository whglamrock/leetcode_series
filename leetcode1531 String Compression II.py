from functools import lru_cache

# notice how:
# 1) the length increase for the compressed string is handled when s[i] is deleted
# 2) to gracefully handle some number of repeated letters
class Solution:
    def __init__(self):
        self.s = ''

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.s = s
        return self.dfs(0, "", 0, k)

    # remember the dfs doesn't count the length of compressed s[:i]
    @lru_cache(None)
    def dfs(self, i: int, prevChar: str, charCount: int, k: int):
        if k < 0:
            return 2147483647
        if i >= len(self.s):
            return 0

        if self.s[i] == prevChar:
            # don't delete char here because the below "lengthOfDeleteChar" case covered it.
            # e.g., for 'bcaaaaaaaaaa' and k = 11 you can delete 9 a's and based on our logic
            # the case of deleting of 9 consecutive 'a's will just be covered when prevChar = c and
            # the first 9 'a's will be deleted.
            lengthIncrease = 1 if charCount in [1, 9, 99] else 0
            return lengthIncrease + self.dfs(i + 1, prevChar, charCount + 1, k)
        else:
            lengthOfKeepChar = 1 + self.dfs(i + 1, self.s[i], 1, k)
            lengthOfDeleteChar = self.dfs(i + 1, prevChar, charCount, k - 1)
            return min(lengthOfKeepChar, lengthOfDeleteChar)
