from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(TrieNode)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                curr = curr.children[char]
                curr.count += 1

        ans = [0] * len(words)
        for i, word in enumerate(words):
            curr = root
            for char in word:
                curr = curr.children[char]
                ans[i] += curr.count
        return ans


print(Solution().sumPrefixScores(words=["abc", "ab", "bc", "b"]))


'''
# original naive hashmap solution
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        stringToScore = defaultdict(int)
        wordToPrefixes = defaultdict(set)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                
                stringToScore[prefix] += 1
                wordToPrefixes[word].add(prefix)
        
        ans = [0] * len(words)
        for i, word in enumerate(words):
            for prefix in wordToPrefixes[word]:
                ans[i] += stringToScore[prefix]
        return ans
'''
