from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.matchingWords = set()

class WordFilter:
    def __init__(self, words: List[str]):
        self.prefixRoot, self.suffixRoot = TrieNode(), TrieNode()
        self.wordToIndex = {}
        for i, word in enumerate(words):
            self.insertWord(word, self.prefixRoot, False)
            self.insertWord(word[::-1], self.suffixRoot, True)
            # always update the index of the same word to the largest index
            self.wordToIndex[word] = i

    def insertWord(self, word: str, root: TrieNode, isReverse: bool):
        curr = root
        for char in word:
            curr = curr.children[char]
            if isReverse:
                curr.matchingWords.add(word[::-1])
            else:
                curr.matchingWords.add(word)

    def f(self, pref: str, suff: str) -> int:
        curr = self.prefixRoot
        for char in pref:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        wordsFromPrefix = curr.matchingWords
        if not wordsFromPrefix:
            return -1

        curr = self.suffixRoot
        for char in suff[::-1]:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        wordsFromSuffix = curr.matchingWords
        if not wordsFromSuffix:
            return -1

        wordCandidates = wordsFromPrefix.intersection(wordsFromSuffix)
        if not wordCandidates:
            return -1
        return max(self.wordToIndex[word] for word in wordCandidates)
