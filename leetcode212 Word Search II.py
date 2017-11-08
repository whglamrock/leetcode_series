
# the idea of using trie is to 'save' the space.
# Trie in worst case takes O(26^m) space complexity where the m is the length of longest word.
# Using a hashset to keep the words takes O(k*n) space where the k is the average length of word
#   and the n is number of words.

from _collections import defaultdict
from copy import deepcopy

class TrieNode(object):
    def __init__(self):
        self.isword = False
        self.children = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addword(self, word):
        cur = self.root
        for letter in word:
            cur  = cur.children[letter]
        cur.isword = True

# Directly used the Trie implementation from lc208. However, the 'searchword' function
# has beeN removed because it's useless in this question.
# DFS solution. Discussing the time/space doesn't make much sense here: even
# with optimization the time could still be exponential in worst case

class Solution(object):
    def findWords(self, board, words):

        if not board or len(board[0]) == 0 or (not words): return []

        self.board = deepcopy(board)
        self.res = []
        self.trie = Trie()

        for word in words:
            self.trie.addword(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                # if we make the path a list, it will be slower than a string
                self.dfs(i, j, self.trie.root, '')

        return self.res

    def dfs(self, i, j, node, path):

        if node.isword:
            self.res.append(path)
            # the words input in findwords function might contain duplicates
            node.isword = False

        # invalid input
        if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]):
            return

        tmp = self.board[i][j]
        if tmp not in node.children:
            return
        node = node.children[tmp]
        # this step has to be after the if statement check because if the program ends, the
        # self.board[i][j] = '#' will be changed permanently
        self.board[i][j] = '#'  # or it can be any character other than lower letters

        # the performance of using string for path is better, probably because the
        # recursion needs to pass the list path to next recursion, which is more time
        # consuming than passing a string
        self.dfs(i - 1, j, node, path + tmp)
        self.dfs(i + 1, j, node, path + tmp)
        self.dfs(i, j - 1, node, path + tmp)
        self.dfs(i, j + 1, node, path + tmp)
        self.board[i][j] = tmp

