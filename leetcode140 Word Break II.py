from functools import lru_cache
from typing import List

class Solution:
    def __init__(self):
        self.wordDict = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)
        return self.dfs(s, 0)

    @lru_cache(None)
    def dfs(self, s: str, i: int) -> List[str]:
        if i == len(s):
            return ['']

        ans = []
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in self.wordDict:
                wordBreaksOfSuffix = self.dfs(s, j)
                for wordBreakOfSuffix in wordBreaksOfSuffix:
                    ans.append((s[i:j] + ' ' + wordBreakOfSuffix).strip())
        return ans


print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog", "an", "ddog"]))
print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(Solution().wordBreak("aaaaaaaa", ["a", 'aa', "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"]))
