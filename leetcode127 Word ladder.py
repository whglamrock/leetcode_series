from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        todo = {beginWord}
        lenOfSequence = 1
        while todo:
            nextTodo = set()
            for word in todo:
                if word == endWord:
                    return lenOfSequence
                for i in range(len(word)):
                    for adjacentWord in self.generateAdjacentWords(word, i, wordList):
                        nextTodo.add(adjacentWord)

            todo = nextTodo
            lenOfSequence += 1

        return 0

    def generateAdjacentWords(self, word: str, i: int, wordList: set) -> set:
        adjacentWords = set()
        for char in 'abcdefghijklmnopqrstuvwxyz':
            adjacentWord = word[:i] + char + word[i + 1:]
            if adjacentWord in wordList:
                adjacentWords.add(adjacentWord)
                wordList.discard(adjacentWord)

        return adjacentWords


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
