from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.words = set()
        self.children = defaultdict(TrieNode)


# this one is intuit phone screen question, originally from: https://www.1point3acres.com/bbs/thread-1062353-1-1.html
class OneToOneStringCompression:
    def __init__(self):
        self.lenToRoot = defaultdict(TrieNode)

    def compressStrs(self, strings: List[str]) -> List[str]:
        # add all words to trie
        for word in strings:
            root = self.lenToRoot[len(word)]
            curr = root
            for char in word:
                curr = curr.children[char]
                curr.words.add(word)

        ans = []
        for word in strings:
            lenOfNonOverlapping = self.findLenOfNonOverlappingPrefix(word)
            if lenOfNonOverlapping < len(word) - 2:
                ans.append(word[:lenOfNonOverlapping] + str(len(word) - lenOfNonOverlapping - 1) + word[-1])
            else:
                ans.append(word)

        return ans

    def findLenOfNonOverlappingPrefix(self, word: str) -> int:
        lenOfNonOverlapping = 0
        root = self.lenToRoot[len(word)]
        curr = root
        for char in word:
            curr = curr.children[char]
            lenOfNonOverlapping += 1
            if len(curr.words) == 1:
                break

        return lenOfNonOverlapping


print(OneToOneStringCompression().compressStrs(['bobble', 'boggle', 'bcdefg', 'abcd', 'yasdjahd', 'bobble']))
print(OneToOneStringCompression().compressStrs(['b', 'bb', 'bbb', 'bbbb', 'bbbbb']))
