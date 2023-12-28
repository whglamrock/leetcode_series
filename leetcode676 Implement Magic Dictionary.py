from collections import defaultdict
from typing import List

class MagicDictionary:
    def __init__(self):
        self.magicDict = defaultdict(int)
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.add(word)
            for i in range(len(word)):
                regexWord = word[:i] + '*' + word[i + 1:]
                self.magicDict[regexWord] += 1

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            regexWord = searchWord[:i] + '*' + searchWord[i + 1:]
            if regexWord in self.magicDict:
                if self.magicDict[regexWord] > 1 or (self.magicDict[regexWord] == 1 and searchWord not in self.words):
                    return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

'''
# Trie Solution
class TrieNode:
    def __init__(self):
        self.numOfWords = 0
        # a char to trieNode map
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode()
                node.children[char] = newNode
                node = newNode
        node.numOfWords += 1
                
    def search(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.numOfWords

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.add(word)
            for i in range(len(word)):
                regexWord = word[:i] + '*' + word[i + 1:]
                self.trie.insert(regexWord)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            regexWord = searchWord[:i] + '*' + searchWord[i + 1:]
            numOfHits = self.trie.search(regexWord)
            if numOfHits == 0:
                continue
            if numOfHits > 1 or (numOfHits == 1 and searchWord not in self.words):
                return True
        
        return False
'''
