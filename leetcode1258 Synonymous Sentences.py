from collections import defaultdict
from typing import List, Dict

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        similarWords = defaultdict(set)
        for s, t in synonyms:
            similarWords[s].add(t)
            similarWords[t].add(s)
        connectedSynonyms = self.generateConnectedSynonyms(similarWords)

        words = text.split(' ')
        curr = ['']
        for word in words:
            next = []
            if word not in connectedSynonyms:
                for subStr in curr:
                    next.append(subStr + ' ' + word)
            else:
                for similarWord in connectedSynonyms[word]:
                    for subStr in curr:
                        next.append(subStr + ' ' + similarWord)
            curr = next

        ans = []
        for string in curr:
            ans.append(string.strip())
        return sorted(ans)

    def generateConnectedSynonyms(self, similarWords: Dict[str, set]) -> Dict[str, set]:
        connectedSynonyms = {}
        visited = set()

        for word in similarWords:
            if word in visited:
                continue

            connectedWords = set()
            todo = {word}
            while todo:
                nextTodo = set()
                for currWord in todo:
                    visited.add(currWord)
                    connectedWords.add(currWord)
                    if currWord not in similarWords:
                        continue
                    for nextWord in similarWords[currWord]:
                        if nextWord not in visited:
                            nextTodo.add(nextWord)
                todo = nextTodo

            for connectedWord in connectedWords:
                connectedSynonyms[connectedWord] = connectedWords

        return connectedSynonyms


print(Solution().generateSentences(synonyms=[["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]],
                                   text="I am happy today but was sad yesterday"))
