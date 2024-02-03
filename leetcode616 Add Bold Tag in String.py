from typing import List, Optional

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        words.sort(key=lambda x: -len(x))
        prevLeft, prevRight = None, None
        boldTagLeftIndexes = set()
        boldTagRightIndexes = set()
        for i in range(len(s)):
            matchingWord = self.findMatchingWord(s, i, words)
            if matchingWord is not None:
                currLeft, currRight = i, i + len(matchingWord) - 1
                if prevLeft is None:
                    prevLeft, prevRight = currLeft, currRight
                elif currLeft > prevRight + 1:
                    boldTagLeftIndexes.add(prevLeft)
                    boldTagRightIndexes.add(prevRight)
                    prevLeft, prevRight = currLeft, currRight
                else:
                    prevRight = max(currRight, prevRight)
        if prevRight:
            boldTagLeftIndexes.add(prevLeft)
            boldTagRightIndexes.add(prevRight)

        ans = []
        for i in range(len(s)):
            if i in boldTagLeftIndexes:
                ans.append('<b>')
            ans.append(s[i])
            if i in boldTagRightIndexes:
                ans.append('</b>')
        return ''.join(ans)

    def findMatchingWord(self, s: str, i: int, words: List[str]) -> Optional[str]:
        for word in words:
            if s.startswith(word, i):
                return word
        return None
