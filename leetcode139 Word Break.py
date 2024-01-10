from functools import lru_cache
from typing import List

class Solution:
    def __init__(self):
        self.wordDict = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        return self.dfs(s)

    @lru_cache(None)
    def dfs(self, substring: str) -> bool:
        if not substring:
            return True

        for i in range(1, len(substring) + 1):
            if substring[:i] in self.wordDict and self.dfs(substring[i:]):
                return True

        return False


print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))


'''
class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        # dp[i] means whether s[:i] can be constructed by words in wordDict
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
'''
