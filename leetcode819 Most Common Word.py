
from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        wordCount = defaultdict(int)
        banned = set(banned)
        curr = []
        for char in paragraph:
            if not char.isalpha():
                if curr:
                    word = "".join(curr)
                    wordCount[word] += 1
                    curr = []
            else:
                curr.append(char.lower())
        if curr:
            wordCount["".join(curr)] += 1

        maxCount = 0
        res = ''
        for word in wordCount:
            if wordCount[word] > maxCount and word not in banned:
                maxCount = wordCount[word]
                res = word

        return res



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print Solution().mostCommonWord(paragraph, banned)
