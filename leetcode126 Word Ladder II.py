
from collections import defaultdict
from copy import deepcopy

# the core idea is use a word -> distance map to make sure the distance is shortest for each visited word

class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):

        wordToNeighbors = {}
        wordSet = set(wordList)
        distance = {}  # word -> distance map that can be used to check visited
        self.bfs(beginWord, endWord, wordToNeighbors, wordSet, distance)

        distanceToWords = defaultdict(list)
        for word in distance:
            dist = distance[word]
            distanceToWords[dist].append(word)

        if endWord not in distance:
            return []
        ans = []
        self.dfs(ans, [], endWord, beginWord, wordToNeighbors, distance)
        return ans

    # pass an empty map to get the wordToNeighbors maping
    def bfs(self, beginWord, endWord, wordToNeighbors, wordSet, distance):
        distance[beginWord] = 0
        todo = set([beginWord])

        while todo:
            next = set()
            for currWord in todo:
                currDist = distance.get(currWord)
                # only search for neighbors for necessary currWord
                neighbors = self.getNeighbors(wordSet, currWord)
                wordToNeighbors[currWord] = neighbors
                for nextWord in neighbors:
                    if nextWord not in distance:  # very important and makes sure the distance is shortest
                        distance[nextWord] = currDist + 1
                        next.add(nextWord)
            todo = next
            if endWord in todo:
                break

    # return a list
    def getNeighbors(self, wordSet, currWord):
        neighbors = []
        workBreak = list(currWord)
        for i in xrange(len(currWord)):
            for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']:
                if c == currWord[i]:
                    continue
                workBreak[i] = c
                newWord = ''.join(workBreak)
                if newWord in wordSet:
                    neighbors.append(newWord)
                workBreak[i] = currWord[i]
        return neighbors

    # prepare the ans
    def dfs(self, ans, solution, endWord, currWord, wordToNeighbors, distance):
        solution.append(currWord)
        if currWord == endWord:
            ans.append(deepcopy(solution))  # otherwise "solution.pop()" will make it always empty
        else:
            if currWord in wordToNeighbors:
                for nextWord in wordToNeighbors[currWord]:
                    if distance[nextWord] == distance[currWord] + 1:
                        self.dfs(ans, solution, endWord, nextWord, wordToNeighbors, distance)
        solution.pop()



Sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print Sol.findLadders(beginWord, endWord, wordList)


