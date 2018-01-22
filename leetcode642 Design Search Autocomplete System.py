
from collections import defaultdict

# counts need to be added to retrieve the sentence and count, even though there are many repeated sentences

class TrieNode:

    def __init__(self):

        self.children = defaultdict(TrieNode)
        self.counts = defaultdict(int)


class AutocompleteSystem(object):

    def __init__(self, sentences, times):

        self.root = TrieNode()
        self.prefix = ""
        for s, count in zip(sentences, times):
            self.add(s, count)

    def add(self, s, count):
        curr = self.root
        for c in s:
            curr = curr.children[c]
            curr.counts[s] += count

    def input(self, c):

        # even when the prefix exists in trie, we need to return []
        if c == "#":
            self.add(self.prefix, 1)
            # reset but don't clear the root, because we can multiple rounds of inputs (multiple "#"s)
            self.prefix = ""
            return []

        # locate the right place in trie
        self.prefix += c
        curr = self.root
        for char in self.prefix:
            # as long as the char != "#", we don't need to call add()
            if char not in curr.children:
                return []
            curr = curr.children[char]

        # add the corresponding sentences and counts to answer
        pq = []
        for s in curr.counts:
            pq.append([-curr.counts[s], s])
        pq.sort()

        res = []
        for i in xrange(min(3, len(pq))):
            res.append(pq[i][1])

        return res