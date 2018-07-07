
from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        paragraph = paragraph.split(' ')
        wordCount = defaultdict(int)
        banned = set(banned)
        symbols = "!?',;."
        for word in paragraph:
            for symbol in symbols:
                word = word.strip(symbol)
            word = word.lower()
            if word and word not in banned:
                wordCount[word.lower()] += 1

        maxCount = 0
        res = ''
        for word, count in wordCount.iteritems():
            if count > maxCount:
                maxCount = count
                res = word

        return res



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print Solution().mostCommonWord(paragraph, banned)
