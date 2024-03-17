from collections import Counter
from copy import deepcopy
from typing import List, Dict

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        charCount = Counter(s)
        oddCountChars = self.getOddCountChars(charCount)
        if len(oddCountChars) > 1:
            return []

        if len(oddCountChars) == 0:
            todo = [['', charCount]]
        else:
            charCount[oddCountChars[0]] -= 1
            if not charCount[oddCountChars[0]]:
                del charCount[oddCountChars[0]]
            todo = [[oddCountChars[0], charCount]]

        ans = set()
        visited = set()
        while todo:
            nextTodo = []
            for currStr, currCharCount in todo:
                visited.add(currStr)
                if not currCharCount:
                    ans.add(currStr)
                for nextChar in currCharCount:
                    nextStr = nextChar + currStr + nextChar
                    if nextStr in visited:
                        continue
                    visited.add(nextStr)
                    nextCharCount = deepcopy(currCharCount)
                    nextCharCount[nextChar] -= 2
                    if not nextCharCount[nextChar]:
                        del nextCharCount[nextChar]
                    nextTodo.append([nextStr, nextCharCount])

            todo = nextTodo

        return list(ans)

    def getOddCountChars(self, charCount: Dict[str, int]) -> List[str]:
        oddCountChars = []
        for char in charCount:
            if charCount[char] % 2:
                oddCountChars.append(char)
        return oddCountChars


print(Solution().generatePalindromes('aaaabb'))
