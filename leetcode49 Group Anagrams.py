
from collections import Counter, defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        keyToAnagrams = defaultdict(list)
        for string in strs:
            key = self.getAnagramKey(string)
            keyToAnagrams[key].append(string)

        return list(keyToAnagrams.values())

    def getAnagramKey(self, string):
        letterCount = Counter(string)
        key = []
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter in letterCount:
                key.append(letter + str(letterCount[letter]))

        return ''.join(key)



print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
