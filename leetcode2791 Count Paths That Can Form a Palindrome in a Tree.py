from collections import defaultdict
from copy import deepcopy
from typing import Dict, List

# The stupid leetcode only accepts O(N) solution which is unachievable without using bitmask.
# Below O(N ^ 2) solution is definitely OK in real interview. See idea: https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/solutions/3803762/java-c-python-bit-mask/
class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        nodeToChildren = defaultdict(set)
        for i, parentI in enumerate(parent):
            nodeToChildren[parentI].add(i)

        nodeToCharCount = {}
        todo = [[0, defaultdict(int)]]
        visited = set()
        while todo:
            nextTodo = []
            for node, currCharCount in todo:
                if node in visited:
                    continue
                nodeToCharCount[node] = currCharCount
                visited.add(node)
                for child in nodeToChildren[node]:
                    if child in visited:
                        continue
                    nextCharCount = deepcopy(currCharCount)
                    nextCharCount[s[child]] += 1
                    nextTodo.append([child, nextCharCount])

            todo = nextTodo

        del nodeToCharCount[0]

        pathCount = 0
        for node1 in nodeToCharCount:
            if self.isCharCountPalindrome(nodeToCharCount[node1]):
                pathCount += 1
            for node2 in nodeToCharCount:
                if node2 <= node1:
                    continue
                # only doing deepcopy here instead of in above loop because
                # otherwise the charCount1 will be changed across the inner for loops.
                charCount1 = deepcopy(nodeToCharCount[node1])
                charCount2 = deepcopy(nodeToCharCount[node2])
                mergedCharCount = self.merge2CharCounts(charCount1, charCount2)
                if self.isCharCountPalindrome(mergedCharCount):
                    pathCount += 1

        return pathCount

    def merge2CharCounts(self, charCount1: Dict[str, int], charCount2: Dict[str, int]) -> Dict[str, int]:
        charCount = charCount1
        for char, count in charCount2.items():
            charCount[char] += count
        return charCount

    def isCharCountPalindrome(self, charCount: Dict[str, int]) -> bool:
        oddCountNode = 0
        for count in charCount.values():
            if count % 2:
                oddCountNode += 1
        return oddCountNode <= 1
