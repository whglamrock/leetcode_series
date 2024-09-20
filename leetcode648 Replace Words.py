from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.root = ''
        self.children = defaultdict(TrieNode)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trieRoot = TrieNode()
        for word in dictionary:
            curr = trieRoot
            for char in word:
                curr = curr.children[char]
            curr.root = word

        ans = []
        words = sentence.split(' ')
        for word in words:
            matchedRoot = self.dfs(trieRoot, word, 0)
            if matchedRoot:
                ans.append(matchedRoot)
            else:
                ans.append(word)

        return ' '.join(ans)

    def dfs(self, currNode: TrieNode, searchWord: str, currIndex: int) -> str:
        # prefix matched to a root
        if currNode.root:
            return currNode.root

        if currIndex == len(searchWord) or searchWord[currIndex] not in currNode.children:
            return currNode.root

        return self.dfs(currNode.children[searchWord[currIndex]], searchWord, currIndex + 1)
