from collections import defaultdict
from typing import List

# The stupid leetcode is giving Memory limit exceeded rn for below solution. What is fucking wrong with leetcode?
# Below solution will be 100% accepted in real interview.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        todo = {beginWord}
        wordToNextWord = defaultdict(set)
        steps = 0
        foundEndWord = False
        while todo:
            nextTodo = set()
            for word in todo:
                wordList.discard(word)
                for nextWord in self.getNeighbors(word, wordList):
                    if nextWord not in wordToNextWord:
                        nextTodo.add(nextWord)
                        wordToNextWord[word].add(nextWord)
            if endWord in nextTodo:
                foundEndWord = True
                break
            todo = nextTodo
            steps += 1

        if not foundEndWord:
            return []

        curr = [[beginWord]]
        for i in range(steps):
            next = []
            for wordChain in curr:
                for nextWord in wordToNextWord[wordChain[-1]]:
                    next.append(wordChain + [nextWord])
            curr = next

        ans = []
        for wordChain in curr:
            if endWord in wordToNextWord[wordChain[-1]]:
                ans.append(wordChain + [endWord])
        return ans

    def getNeighbors(self, word: str, wordList: set) -> set:
        neighbors = set()
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char != word[i]:
                    neighbor = word[:i] + char + word[i + 1:]
                    if neighbor in wordList:
                        neighbors.add(neighbor)
        return neighbors


print(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
