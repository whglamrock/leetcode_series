
# Trie data structure demo: https://www.youtube.com/watch?v=AXjmTQ8LEoI

from collections import defaultdict

class TrieNode(object):

    def __init__(self):

        self.children = defaultdict(TrieNode)
        self.isword = False


class Trie(object):

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):

        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isword = True

    def search(self, word):

        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return current.isword

    def startsWith(self, word):

        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return True



# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
