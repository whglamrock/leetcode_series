from typing import List, Set

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        wordToIndex = {}
        for i, word in enumerate(words):
            wordToIndex[word] = i

        # dp[i] means the length of the longest char ends at words[i]
        dp = [1] * len(words)
        for i, word in enumerate(words):
            for predecessor in self.generatePredecessors(word):
                if predecessor in wordToIndex:
                    j = wordToIndex[predecessor]
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def generatePredecessors(self, word: str) -> Set[str]:
        predecessors = set()
        for i in range(len(word)):
            predecessors.add(word[:i] + word[i + 1:])
        return predecessors


print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
