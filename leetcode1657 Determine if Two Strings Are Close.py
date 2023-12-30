from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        wordCount1 = Counter(word1)
        wordCount2 = Counter(word2)
        valueCount1 = Counter(wordCount1.values())
        valueCount2 = Counter(wordCount2.values())
        charSet1 = set([c for c in word1])
        charSet2 = set([c for c in word2])
        return valueCount1 == valueCount2 and charSet1 == charSet2


print(Solution().closeStrings(word1="abc", word2="bca"))
print(Solution().closeStrings(word1="a", word2="aa"))
print(Solution().closeStrings(word1="cabbba", word2="abbccc"))
print(Solution().closeStrings(word1="uau", word2="ssx"))
