from functools import lru_cache
from typing import List


class Solution:
    def __init__(self):
        self.wordDict = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)
        return self.dfs(s)

    @lru_cache(None)
    def dfs(self, s: str) -> List[str]:
        if not s:
            return ['']

        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] in self.wordDict:
                wordBreaksOfSuffix = self.dfs(s[i:])
                for wordBreakOfSuffix in wordBreaksOfSuffix:
                    ans.append((s[:i] + ' ' + wordBreakOfSuffix).strip())

        return ans


print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog", "an", "ddog"]))
print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(Solution().wordBreak("aaaaaaaa", ["a", 'aa', "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"]))
