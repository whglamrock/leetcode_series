
from collections import defaultdict

class TrieNode:

    def __init__(self):

        self.children = defaultdict(TrieNode)
        # not exactly the weights, but storing the words with this prefix
        self.weights = set()


class WordFilter(object):

    def __init__(self, words):

        self.words = words
        self.wordToWeight = {}
        # Trie1 stores in natural order
        self.root1 = TrieNode()
        # Trie2 stores in reverse order
        self.root2 = TrieNode()
        for i, w in enumerate(words):
            self.add(self.root1, w, False)
            self.add(self.root2, w[::-1], True)
            self.wordToWeight[w] = i

    def add(self, root, w, isReverse):

        curr = root
        for c in w:
            curr = curr.children[c]
            if isReverse:
                curr.weights.add(w[::-1])
            else:
                curr.weights.add(w)

    def f(self, prefix, suffix):

        maxWeight = 0
        wordsWithPrefix = set()
        wordsWithSuffix = set()

        # find the right spot
        curr = self.root1
        for c in prefix:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        # add all the words with this prefix to the wordsWithPrefix
        #   remember the corner case where prefix is an empty String
        if prefix:
            for w in curr.weights:
                wordsWithPrefix.add(w)
        else:
            wordsWithPrefix = set(self.words)

        # find the right spot
        curr = self.root2
        for c in suffix[::-1]:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        # add the all words with prefix to the wordsWithPrefix
        if suffix:
            for w in curr.weights:
                wordsWithSuffix.add(w)
        else:
            wordsWithSuffix = set(self.words)

        wordCandidates = wordsWithSuffix.intersection(wordsWithPrefix)
        for w in wordCandidates:
            maxWeight = max(maxWeight, self.wordToWeight[w])
        return maxWeight


