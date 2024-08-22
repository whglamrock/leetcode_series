from collections import defaultdict
from typing import List, Dict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = ''


# O(N * m) DFS + Trie solution, where m is the average length of each word
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        words = set(words)
        for word in words:
            curr = root
            # no need to build prefix here
            for char in word:
                curr = curr.children[char]
            curr.word = word

        lenToMinWord = {}
        self.dfs(root, words, lenToMinWord)
        if not lenToMinWord:
            return ''

        return lenToMinWord[max(lenToMinWord.keys())]

    def dfs(self, node: TrieNode, words: set, lenToMinWord: Dict[int, str]):
        if node.word:
            word = node.word
            if len(word) not in lenToMinWord or word < lenToMinWord[len(word)]:
                lenToMinWord[len(word)] = word

        for char in node.children:
            child = node.children[char]
            if not child.word:
                continue
            self.dfs(child, words, lenToMinWord)


print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))
print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
