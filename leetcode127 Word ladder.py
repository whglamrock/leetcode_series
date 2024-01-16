from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        todo = {beginWord}
        lengthOfSequence = 1
        while todo:
            lengthOfSequence += 1
            nextTodo = set()
            for word in todo:
                for i in range(len(word)):
                    for adjacentWord in self.generateAdjacentWords(word, i):
                        if adjacentWord == endWord:
                            return lengthOfSequence
                        if adjacentWord not in wordList:
                            continue
                        nextTodo.add(adjacentWord)
                        wordList.discard(adjacentWord)
            todo = nextTodo

        return 0

    def generateAdjacentWords(self, word: str, i: int) -> List[str]:
        words = []
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char == word[i]:
                continue
            words.append(word[:i] + char + word[i + 1:])
        return words


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
