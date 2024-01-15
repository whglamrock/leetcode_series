from collections import defaultdict
from typing import List, Dict

# the stupid leetcode added a new stupid test case like ['abc', 'ab'] should yield ''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if self.existsAnyInvalidRelationships(words):
            return ''

        greater, less = defaultdict(set), defaultdict(set)
        self.buildRelationShip(words, greater, less)

        todo = set()
        charSet = set()
        for word in words:
            for char in word:
                charSet.add(char)
                if char not in greater:
                    todo.add(char)

        ans = []
        while todo:
            # only stores the chars not in greater at the moment
            nextTodo = set()
            for char in todo:
                ans.append(char)
                # means there are some chars bigger that this char
                if char in less:
                    greaterChars = less[char]
                    for greaterChar in greaterChars:
                        greater[greaterChar].discard(char)
                        if not greater[greaterChar]:
                            nextTodo.add(greaterChar)
                            del greater[greaterChar]
            todo = nextTodo

        return ''.join(ans) if len(ans) == len(charSet) else ''

    # the whole fucking point of this method is to deal with stupid leetcode test cases like ['abc', 'ab']
    def existsAnyInvalidRelationships(self, words: List[str]) -> bool:
        for i in range(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and words[i - 1].startswith(words[i]):
                return True
        return False

    def buildRelationShip(self, words: List[str], greater: Dict[str, set], less: Dict[str, set]):
        for i in range(1, len(words)):
            prevWord, word = words[i - 1], words[i]
            for j in range(min(len(prevWord), len(word))):
                if prevWord[j] == word[j]:
                    continue
                greater[word[j]].add(prevWord[j])
                less[prevWord[j]].add(word[j])
                # we only need to build relationship once in a pair of words
                break


print(Solution().alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]))
