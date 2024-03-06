from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToMaxIndex = {}
        for i, char in enumerate(s):
            charToMaxIndex[char] = i

        ans = []
        i = 0
        while i < len(s):
            l = i
            r = charToMaxIndex[s[i]]
            while i < r:
                r = max(r, charToMaxIndex[s[i]])
                i += 1
            i = r + 1
            ans.append(r - l + 1)

        return ans
