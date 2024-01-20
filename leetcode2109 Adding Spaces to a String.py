from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0
        for i, char in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(char)
        return ''.join(ans)
