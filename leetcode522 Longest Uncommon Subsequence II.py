from collections import defaultdict, Counter
from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: -len(x))
        strCount = Counter(strs)
        strLenToStrings = defaultdict(set)
        for string in strs:
            strLenToStrings[len(string)].add(string)

        for string in strs:
            # if there are more than 1 of such string, it's not our candidate
            if strCount[string] > 1:
                continue

            isCurrStrSubseqOfAnother = False
            for longerLen in range(len(string) + 1, 11):
                if longerLen not in strLenToStrings:
                    continue
                if isCurrStrSubseqOfAnother:
                    break
                for longerString in strLenToStrings[longerLen]:
                    if self.isSubSequenceOfAnother(string, longerString):
                        isCurrStrSubseqOfAnother = True
                        break

            if not isCurrStrSubseqOfAnother:
                return len(string)

        return -1

    def isSubSequenceOfAnother(self, s1: str, s2: str) -> bool:
        i = 0
        for char in s2:
            if i < len(s1) and char == s1[i]:
                i += 1
        return i == len(s1)
