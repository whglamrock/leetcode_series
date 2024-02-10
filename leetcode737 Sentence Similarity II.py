from collections import defaultdict
from typing import List

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        wordsToSimilarWords = defaultdict(set)
        wordSet = set()
        for word1, word2 in similarPairs:
            wordsToSimilarWords[word1].add(word2)
            wordsToSimilarWords[word2].add(word1)
            wordSet.add(word1)
            wordSet.add(word2)

        # bfs
        wordToConnectedWords = {}
        visited = set()
        for word in wordSet:
            if word in visited:
                continue
            todo = {word}
            similarWords = set()
            while todo:
                nextTodo = set()
                for currWord in todo:
                    visited.add(currWord)
                    similarWords.add(currWord)
                    for nextWord in wordsToSimilarWords[currWord]:
                        if nextWord not in visited:
                            nextTodo.add(nextWord)
                todo = nextTodo

            for connectedWord in similarWords:
                wordToConnectedWords[connectedWord] = similarWords

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence1[i] in wordToConnectedWords and sentence2[i] in wordToConnectedWords[sentence1[i]]:
                continue
            if sentence2[i] in wordToConnectedWords and sentence1[i] in wordToConnectedWords[sentence2[i]]:
                continue
            return False

        return True

