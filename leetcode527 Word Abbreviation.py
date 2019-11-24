
from collections import defaultdict

# typical Google type question, also asked by Snap
# O(K * N * log(N)) solution is good enough where K is avg(len(word)).
    # In real interview we can mention it's possible to use Trie to optimize to O(K * N)

class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        abbrToWords = defaultdict(list)
        for word in words:
            abbr = self.getAbbr(word)
            abbrToWords[abbr].append(word)

        wordToAbbr = {}
        for abbr in abbrToWords:
            wordsWithSameAbbr = abbrToWords[abbr]
            if len(wordsWithSameAbbr) == 1:
                wordToAbbr[wordsWithSameAbbr[0]] = abbr
            else:
                wordsWithSameAbbr.sort()
                # except the last word, each word's prefix will be calculated twice
                for i in xrange(len(wordsWithSameAbbr) - 1):
                    word1, word2 = wordsWithSameAbbr[i], wordsWithSameAbbr[i + 1]
                    j = self.getFirstDifferentIndex(word1, word2)
                    prefix1 = word1[:j + 1]
                    prefix2 = word2[:j + 1]

                    # abbreviation is not shorter
                    if len(prefix1) >= len(word1) - 2:
                        wordToAbbr[word1] = word1
                        wordToAbbr[word2] = word2
                    # abbreviation is shorter
                    else:
                        newPrefix1 = prefix1 + str(len(word1) - len(prefix1) - 1) + word1[-1]
                        # when newPrefix1 for word1 is longer than the one calculated from previous loop of comparison, override it
                        if word1 not in wordToAbbr or len(wordToAbbr[word1]) < len(newPrefix1):
                            wordToAbbr[word1] = newPrefix1
                        # no need to override word2 because it's always the first time calculating its prefix
                        wordToAbbr[word2] = prefix2 + str(len(word2) - len(prefix2) - 1) + word2[-1]

        ans = []
        for word in words:
            ans.append(wordToAbbr[word])
        return ans

    def getFirstDifferentIndex(self, word1, word2):
        i = 0
        # word1 and word2 must have same length
        n = len(word1)
        while i < n and word1[i] == word2[i]:
            i += 1
        return i

    def getAbbr(self, word):
        if len(word) <= 3:
            return word
        return word[0] + str(len(word) - 2) + word[-1]



print Solution().wordsAbbreviation(["abcdefg", "abccefg", "abcckkg"])
print Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion", "intrution"])