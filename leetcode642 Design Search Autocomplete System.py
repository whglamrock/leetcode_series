from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.counts = defaultdict(int)


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        for sentence, count in zip(sentences, times):
            self.addSentence(sentence, count)
        self.prefix = []
        self.foundMatchForPrefix = True

    def addSentence(self, sentence: str, count: int):
        curr = self.root
        for char in sentence:
            curr = curr.children[char]
            curr.counts[sentence] += count

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.addSentence(''.join(self.prefix), 1)
            self.prefix = []
            self.curr = self.root
            self.foundMatchForPrefix = True
            return []

        self.prefix.append(c)
        if c not in self.curr.children or not self.foundMatchForPrefix:
            self.foundMatchForPrefix = False
            return []

        self.curr = self.curr.children[c]
        candidates = []
        for sentence, count in self.curr.counts.items():
            candidates.append([-count, sentence])
        # can be optimized by using 3 variables to track max, second max and 3rd max count & corresponding sentences
        candidates.sort()

        ans = []
        for i in range(min(3, len(candidates))):
            ans.append(candidates[i][1])

        return ans
