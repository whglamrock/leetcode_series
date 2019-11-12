# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

from collections import defaultdict

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        if not wordlist:
            return

        # this is for the convenience of calculating next candidates
        wordToMatchLenToWords = {}
        for i, word1 in enumerate(wordlist):
            wordToMatchLenToWords[word1] = defaultdict(list)
            for j, word2 in enumerate(wordlist):
                if i == j or word1 == word2:
                    continue
                matchLen = self.calculateMatchlength(word1, word2)
                wordToMatchLenToWords[word1][matchLen].append(word2)

        #
        singleCharCount = [[0 for j in xrange(26)] for i in xrange(6)]
        for word in wordlist:
            for i, char in enumerate(word):
                singleCharCount[i][ord(char) - ord('a')] += 1

        candidates = set(wordlist)
        while candidates:
            nextcandidates = set()
            bestScore = 0
            bestWord = None
            # get the word with best score
            for word in candidates:
                score = self.getScore(word, singleCharCount)
                if score > bestScore:
                    bestWord = word
                    bestScore = score
            if bestWord:
                matchLenWithSecret = master.guess(bestWord)
                for newCandidate in wordToMatchLenToWords[bestWord][matchLenWithSecret]:
                    if newCandidate in candidates:
                        nextcandidates.add(newCandidate)
            candidates = nextcandidates

    def getScore(self, word, singleCharCount):
        score = 0
        for i, char in enumerate(word):
            score += singleCharCount[i][ord(char) - ord('a')]
        return score

    def calculateMatchlength(self, word1, word2):
        count = 0
        for i in xrange(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        return count