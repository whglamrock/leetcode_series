from math import ceil
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        currLen = 0
        curr = []
        for word in words:
            if currLen + len(word) > maxWidth:
                lines.append(curr)
                curr = [word]
                currLen = len(word) + 1
            else:
                curr.append(word)
                currLen += len(word) + 1
        if curr:
            lines.append(curr)

        ans = []
        for i, line in enumerate(lines):
            numOfSpaces = maxWidth - sum(len(word) for word in line)
            justifiedText = []

            # last line needs to be special-cased
            if i < len(lines) - 1:
                for j in range(len(line)):
                    justifiedText.append(line[j])
                    if j < len(line) - 1:
                        numOfSpacesAssigned = ceil(numOfSpaces / (len(line) - j - 1))
                        numOfSpaces -= numOfSpacesAssigned
                        justifiedText.append(' ' * numOfSpacesAssigned)
                    else:
                        if numOfSpaces:
                            justifiedText.append(' ' * numOfSpaces)
            else:
                for j in range(len(line)):
                    justifiedText.append(line[j])
                    if numOfSpaces:
                        justifiedText.append(' ')
                        numOfSpaces -= 1
                if numOfSpaces:
                    justifiedText.append(' ' * numOfSpaces)

            ans.append(''.join(justifiedText))

        return ans


print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
