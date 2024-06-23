from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        startIndexToSourceStrLen = {}
        startIndexToTargetStr = {}
        for startIndex, sourceStr, targetStr in zip(indices, sources, targets):
            length = len(sourceStr)
            if s[startIndex:startIndex + length] != sourceStr:
                continue
            startIndexToSourceStrLen[startIndex] = length
            startIndexToTargetStr[startIndex] = targetStr

        i = 0
        ans = []
        while i < len(s):
            if i not in startIndexToSourceStrLen:
                ans.append(s[i])
                i += 1
                continue

            ans.append(startIndexToTargetStr[i])
            i = i + startIndexToSourceStrLen[i]

        return ''.join(ans)
