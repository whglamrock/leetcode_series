from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        lenOfSqns = 1
        todo = {beginWord}
        while todo:
            nextTodo = set()
            for word in todo:
                if word == endWord:
                    return lenOfSqns
                for i in range(len(word)):
                    neighbors = self.generateNeighborWords(word, i, wordList)
                    nextTodo = nextTodo.union(neighbors)

            todo = nextTodo
            lenOfSqns += 1

        return 0

    def generateNeighborWords(self, word: str, i: int, wordList: set) -> set:
        neighbors = set()
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter == word[i]:
                continue
            neighborWord = word[:i] + letter + word[i + 1:]
            if neighborWord in wordList:
                wordList.discard(neighborWord)
                neighbors.add(neighborWord)

        return neighbors


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
