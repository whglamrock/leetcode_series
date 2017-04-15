
# In worst case same time complexity is O(26^N), space complexity is O(26^N).
#   but the overall/average space complexity is still better than the set solution
# Generally, number of words usually are longer than the length of a single word

from _collections import defaultdict

class TrieNode(object):
    def __init__(self):

        self.isword = False
        self.children = defaultdict(TrieNode)


class WordDictionary(object):
    def __init__(self):

        self.root = TrieNode()

    def addWord(self, word):

        cur = self.root
        for letter in word:
            cur = cur.children[letter]
        cur.isword = True

    def search(self, word):

        return self.searchword(self.root, word, 0)

    def searchword(self, node, word, i):

        if i == len(word):
            return node.isword
        else:
            if word[i] != '.':
                # very important, because if we don't check word[i], the 'node.children[word[i]]'
                # will create a key word[i] in node.children
                if word[i] not in node.children: return False
                return self.searchword(node.children[word[i]], word, i + 1)
            else:
                for child in node.children.values():
                    if self.searchword(child, word, i + 1):
                        return True
                return False



Sol = WordDictionary()
Sol.addWord('bad')
Sol.addWord('dad')
Sol.addWord('mad')
print Sol.search('pad')
print Sol.search('bad')
print Sol.search('b..')



'''
# set solution
# O(1) for search word without '.', O(mn) for search word in worst case when word like '.....'

from _collections import defaultdict
class WordDictionary(object):
    def __init__(self):

        self.dic = defaultdict(set)

    def addWord(self, word):

        self.dic[len(word)].add(word)


    def search(self, word):

        if not word or len(word) not in self.dic:
            return False
        if '.' not in word:
            return word in self.dic[len(word)]

        for addedword in self.dic[len(word)]:
            for i, letter in enumerate(addedword):
                if letter != word[i] and word[i] != '.':
                    break
            else:
                return True

        return False
'''


