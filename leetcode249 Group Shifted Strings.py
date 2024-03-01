from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        sequenceToStrings = defaultdict(list)
        for string in strings:
            if len(string) == 1:
                sequenceToStrings['noDist'].append(string)
            else:
                sequence = []
                for i in range(len(string) - 1):
                    # for cases like za -> ab; az -> ba, try to convert distance to positive number
                    firstChar, secondChar = string[i], string[i + 1]
                    dist = ord(secondChar) - ord(firstChar)
                    dist = (dist + 26) % 26
                    sequence.append(str(dist))
                sequenceToStrings[','.join(sequence)].append(string)

        ans = []
        for groupedStrings in sequenceToStrings.values():
            ans.append(groupedStrings)
        return ans


print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
