from typing import List

# O(N^3) time dp solution
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


print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))


'''
from functools import lru_cache
from typing import List

# cached dfs solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        return self.dfs(s, 0)

    @lru_cache(None)
    def dfs(self, s: str, index: int) -> bool:
        if index == len(s):
            return True
        
        isWordBreakable = False
        for i in range(index + 1, len(s) + 1):
            if s[index:i] in self.wordDict:
                isWordBreakable |= self.dfs(s, i)
                if isWordBreakable:
                    break
        
        return isWordBreakable
'''
