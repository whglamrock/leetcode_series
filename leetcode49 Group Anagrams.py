from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCountStrToWords = defaultdict(list)
        for word in strs:
            charCountStr = self.generateCharCountStr(word)
            charCountStrToWords[charCountStr].append(word)

        ans = []
        for charCountStr in charCountStrToWords:
            ans.append(charCountStrToWords[charCountStr])
        return ans

    def generateCharCountStr(self, word: str) -> str:
        charCount = Counter(word)
        ans = []
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char not in charCount:
                continue
            ans.append(char + str(charCount[char]))
        return ''.join(ans)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
