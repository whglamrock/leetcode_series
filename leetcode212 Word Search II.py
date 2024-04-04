from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        # directly store the word in the node. Otherwise you will have to add char to the path in the bfs search
        # which rebuilds the path string in every recursion.
        self.word = ''
        self.children = defaultdict(TrieNode)

class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                curr = curr.children[c]
            curr.word = word

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, root, board, ans)

        return list(ans)

    def dfs(self, i: int, j: int, curr: 'TrieNode', board: List[List[str]], ans: set):
        if curr.word:
            ans.add(curr.word)
            # do no return here because the word may share a common prefix with other words

        m, n = len(board), len(board[0])
        # the reason for checking i, j here instead of not doing dfs in line 44-47 is because we need
        # one more layer of dfs to trigger curr.isWord == True.
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] not in curr.children:
            return

        # 1) Mark the char unavailable in this dfs, to avoid using a visited set.
        # 2) If you use a visited set, you will need to do visited.discard((i, j)), and even with that in leetcode
        # some edge cases don't work with python
        tmp = board[i][j]
        board[i][j] = '#'

        self.dfs(i - 1, j, curr.children[tmp], board, ans)
        self.dfs(i + 1, j, curr.children[tmp], board, ans)
        self.dfs(i, j - 1, curr.children[tmp], board, ans)
        self.dfs(i, j + 1, curr.children[tmp], board, ans)

        board[i][j] = tmp


# note 2 overlapping words: "eat" and "eatei"
print(Solution().findWords(
    [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ],
    ["oath", "pea", "eat", "rain", "eatei"]))
# this is the stupid leetcode test case where visited set doesn't work, even if you do visited.discard((i, j))
print(Solution().findWords(
    [["e", "e", "c", "d", "b", "b", "c", "b", "c", "d", "e"],
     ["c", "e", "e", "a", "d", "d", "e", "c", "c", "c", "b"],
     ["b", "e", "a", "c", "d", "a", "a", "b", "c", "d", "c"],
     ["e", "d", "e", "d", "c", "c", "e", "b", "d", "e", "e"],
     ["b", "b", "b", "a", "b", "d", "b", "b", "b", "a", "a"],
     ["e", "e", "b", "e", "c", "c", "a", "b", "e", "e", "c"],
     ["b", "a", "b", "c", "b", "d", "a", "d", "c", "d", "a"],
     ["d", "b", "a", "e", "a", "c", "e", "a", "d", "e", "c"]],
    ["aeceecbee"]
))
