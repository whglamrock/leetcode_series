from collections import defaultdict
from typing import List, Dict

# the stupid leetcode added a new stupid test case like ['abc', 'ab'] should yield ''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if self.existsInvalidRelationship(words):
            return ''

        greater, less = defaultdict(set), defaultdict(set)
        self.buildRelationship(words, greater, less)

        todo = set()
        for word in words:
            for char in word:
                # it means no other chars come before this char
                if char not in greater:
                    todo.add(char)

        ans = []
        while todo:
            nextTodo = set()
            for char in todo:
                ans.append(char)
                # it means there are no chars come after this char
                if char not in less:
                    continue
                greaterChars = less[char]
                for greaterChar in greaterChars:
                    if greaterChar not in greater:
                        continue
                    greater[greaterChar].discard(char)
                    if not greater[greaterChar]:
                        del greater[greaterChar]
                        nextTodo.add(greaterChar)
                del less[char]

            todo = nextTodo

        return ''.join(ans) if not less else ''

    def buildRelationship(self, words: List[str], greater: Dict[str, set], less: Dict[str, set]):
        for i in range(len(words) - 1):
            currWord, nextWord = words[i], words[i + 1]
            for j in range(min(len(currWord), len(nextWord))):
                if currWord[j] == nextWord[j]:
                    continue
                greater[nextWord[j]].add(currWord[j])
                less[currWord[j]].add(nextWord[j])
                break

    def existsInvalidRelationship(self, words: List[str]) -> bool:
        for i in range(len(words) - 1):
            currWord, nextWord = words[i], words[i + 1]
            if len(currWord) > len(nextWord) and currWord.startswith(nextWord):
                return True

        return False


print(Solution().alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]))
