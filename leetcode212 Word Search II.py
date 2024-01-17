from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)

class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                curr = curr.children[c]
            curr.isWord = True

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, root, board, '', ans)

        return list(ans)

    def dfs(self, i: int, j: int, curr: 'TrieNode', board: List[List[str]], path: str, ans: set):
        if curr.isWord:
            ans.add(path)
            # do no return here because the word may share a common prefix with other words

        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] not in curr.children:
            return

        # mark the char unavailable in this dfs, to avoid using a visited set
        tmp = board[i][j]
        board[i][j] = '#'

        self.dfs(i - 1, j, curr.children[tmp], board, path + tmp, ans)
        self.dfs(i + 1, j, curr.children[tmp], board, path + tmp, ans)
        self.dfs(i, j - 1, curr.children[tmp], board, path + tmp, ans)
        self.dfs(i, j + 1, curr.children[tmp], board, path + tmp, ans)

        board[i][j] = tmp


print(Solution().findWords(
    [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ],
    ["oath", "pea", "eat", "rain"]))
