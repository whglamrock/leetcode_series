from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isArr1Digit = False
        self.isArr2Digit = False


class Solution:
    def __init__(self):
        self.maxCommonPrefixLen = 0
        self.root = TrieNode()

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        self.root = TrieNode()
        for num in arr1:
            curr = self.root
            for digit in str(num):
                curr = curr.children[digit]
                curr.isArr1Digit = True

        for num in arr2:
            curr = self.root
            for digit in str(num):
                curr = curr.children[digit]
                curr.isArr2Digit = True

        self.maxCommonPrefixLen = 0
        for node in self.root.children.values():
            self.dfs(node, 1)

        return self.maxCommonPrefixLen

    def dfs(self, node: TrieNode, depth: int):
        if not node.isArr1Digit or not node.isArr2Digit:
            return

        self.maxCommonPrefixLen = max(self.maxCommonPrefixLen, depth)
        for childNode in node.children.values():
            self.dfs(childNode, depth + 1)
