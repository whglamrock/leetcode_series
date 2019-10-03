
# One thing we need to get straight before coding: if word0 < word1 and word1 < word2 then word0 must < word2.
# To prove that, assume the index = i where word0/1 differ, and the index = j where word1/2 differ;
    # Then discuss the conditions when i <= j or i > j

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if not words:
            return True

        for i in xrange(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            char1, char2 = self.getFirstDifferentCharPair(word1, word2)
            if not char1 and len(word1) > len(word2):
                return False
            if not char1:
                continue
            if not self.isCorrectOrder(char1, char2, order):
                return False

        return True

    def isCorrectOrder(self, char1, char2, order):
        index1 = 0
        index2 = 0
        while order[index1] != char1:
            index1 += 1
        while order[index2] != char2:
            index2 += 1
        return index1 < index2

    def getFirstDifferentCharPair(self, word1, word2):
        i = 0
        while i < len(word1) and i < len(word2):
            if word1[i] != word2[i]:
                return word1[i], word2[i]
            i += 1
        # means this 2 words are same or one is another's prefix
        return None, None
