from collections import defaultdict
from typing import List

# For cached dfs solution, see at the bottom
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wordsIndexToCharCount = defaultdict(dict)
        for word in words:
            for i, char in enumerate(word):
                if char not in wordsIndexToCharCount[i]:
                    wordsIndexToCharCount[i][char] = 1
                else:
                    wordsIndexToCharCount[i][char] += 1

        m, n = len(target), len(words[0])
        # dp[i][j] means number of ways for to form target[:i] with all word[:j]
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # it's very important to loop the j through all word indexes instead of merely setting dp[0][0] = 1
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            charToMatch = target[i - 1]
            for j in range(1, n + 1):
                # not using word[j - 1] to match target[i - 1]
                dp[i][j] = dp[i][j - 1]
                # use word[j - 1] to match target[i - 1]
                if charToMatch in wordsIndexToCharCount[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1] * wordsIndexToCharCount[j - 1][charToMatch]

        return dp[-1][-1] % (10 ** 9 + 7)


'''
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        self.wordsIndexToCharCount = defaultdict(dict)
        for word in words:
            for i, char in enumerate(word):
                if char not in self.wordsIndexToCharCount[i]:
                    self.wordsIndexToCharCount[i][char] = 1
                else:
                    self.wordsIndexToCharCount[i][char] += 1
        
        wordLen = len(words[0])
        return self.dfs(wordLen, 0, target, 0) % (10 ** 9 + 7)
    
    @lru_cache(None)
    def dfs(self, wordLen: int, wordIndex: int, target: str, targetIndex) -> int:
        if wordLen - wordIndex < len(target) - targetIndex:
            return 0
        if targetIndex == len(target):
            return 1
        
        charToMatch = target[targetIndex]
        ans = 0
        # wordLen - wordIndex >= len(target) - targetIndex ==> wordIndex <= wordLen + targetIndex - len(target)
        for j in range(wordIndex, wordLen + targetIndex - len(target) + 1):
            if charToMatch not in self.wordsIndexToCharCount[j]:
                continue
            ans += self.wordsIndexToCharCount[j][charToMatch] * self.dfs(wordLen, j + 1, target, targetIndex + 1)

        return ans
'''