
from collections import defaultdict

# The idea of using trie is to 'save' the space and enable prefix search.
    # Trie in worst case takes O(26^M) space, where M is the length of longest word.
# Using a set to keep the words takes O(len(words) * avg(len(words[i]))) space
    # and can't prevent invalid DFS because it can't do prefix match search.

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board or not board[0]:
            return []

        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                curr = curr.children[c]
            curr.isWord = True

        # the reason we use set here is we will trigger the line "if curr.isWord: self.ans.add(path)"
            # 4 times, as we rely on line "if i < 0 or i >= m or j < 0 or j >= n:" to filter out the
            # index out of range case
        self.ans = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(i, j, root, board, '')

        return list(self.ans)

    def dfs(self, i, j, curr, board, path):
        if curr.isWord:
            self.ans.add(path)

        m, n = len(board), len(board[0])
        # we do check here instead of right above the dfs, because we need to consider
            # corner case like: [["a"]], ["a"], in which case if we check boundary right
            # before next dfs we won't be able to reach it (but we need to reach the next
            # dfs to trigger the "curr.isWord")
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] not in curr.children:
            return

        # mark the char unavailable in this dfs, to avoid using a visited set
        tmp = board[i][j]
        board[i][j] = '#'

        self.dfs(i - 1, j, curr.children[tmp], board, path + tmp)
        self.dfs(i + 1, j, curr.children[tmp], board, path + tmp)
        self.dfs(i, j - 1, curr.children[tmp], board, path + tmp)
        self.dfs(i, j + 1, curr.children[tmp], board, path + tmp)

        board[i][j] = tmp



print Solution().findWords(
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],
["oath","pea","eat","rain"])