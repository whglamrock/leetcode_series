
from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        symbols = "!?',;. "
        curr = []
        wordCount = defaultdict(int)

        for char in paragraph:
            if char not in symbols:
                curr.append(char.lower())
            else:
                if curr:
                    word = "".join(curr)
                    wordCount[word] += 1
                    curr = []
        if curr:
            wordCount["".join(curr)] += 1

        maxCount = 0
        banned = set(banned)
        res = ''
        for word in wordCount:
            if wordCount[word] > maxCount and word not in banned:
                maxCount = wordCount[word]
                res = word

        return res



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print Solution().mostCommonWord(paragraph, banned)
