from collections import defaultdict
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        wordToSimilarWords = defaultdict(set)
        for i in range(n - 1):
            word1 = strs[i]
            for j in range(i + 1, n):
                word2 = strs[j]
                if self.isSimilar(word1, word2):
                    wordToSimilarWords[word1].add(word2)
                    wordToSimilarWords[word2].add(word1)

        # bfs
        visited = set()
        numOfGroups = 0
        for word in strs:
            if word in visited:
                continue
            todo = {word}
            currVisited = set()
            while todo:
                nextTodo = set()
                for currWord in todo:
                    visited.add(currWord)
                    currVisited.add(currWord)
                    if currWord not in wordToSimilarWords:
                        continue
                    for nextWord in wordToSimilarWords[currWord]:
                        if nextWord not in currVisited:
                            nextTodo.add(nextWord)
                todo = nextTodo
            numOfGroups += 1

        return numOfGroups

    def isSimilar(self, word1: str, word2: str) -> bool:
        diffCount = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffCount += 1
        return diffCount == 0 or diffCount == 2
