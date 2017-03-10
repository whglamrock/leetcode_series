# super easy
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dick = {}
        self.res = 0
        for i in xrange(len(words)):
            if words[i] in self.dick:
                self.dick[words[i]].append(i)
            else:
                self.dick[words[i]] = [i]


    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = 2147483647
        for i in self.dick[word1]:
            for j in self.dick[word2]:
                if abs(i-j)<dist:
                    dist = abs(i-j)

        return dist



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")