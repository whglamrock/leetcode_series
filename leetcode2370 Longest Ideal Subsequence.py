from typing import List


# O(n) dp solution (although it's not a typical dp setup which uses a dp array)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        charToMaxLen = {}
        for char in s:
            currMaxLen = 1 if char not in charToMaxLen else charToMaxLen[char]
            for charWithinDistance in self.findAllCharsWithinDistance(char, k):
                if charWithinDistance not in charToMaxLen:
                    continue
                currMaxLen = max(currMaxLen, charToMaxLen[charWithinDistance] + 1)

            charToMaxLen[char] = currMaxLen

        return max(charToMaxLen.values())

    def findAllCharsWithinDistance(self, char: str, k: int) -> List[str]:
        chars = [char]
        for i in range(ord(char) - k, ord(char)):
            chars.append(chr(i))
        for i in range(ord(char) + 1, ord(char) + k + 1):
            chars.append(chr(i))

        return chars
