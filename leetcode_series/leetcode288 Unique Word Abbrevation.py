# problem description is super vague, see clearance here:
# https://discuss.leetcode.com/topic/37254/let-me-explain-the-question-with-better-examples

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        self.wordset = set(dictionary)
        for word in self.wordset:
            if len(word) <= 2:
                self.dic[word] = 1
            else:
                abbrev = word[0] + str(len(word) - 2) + word[-1]
                if abbrev not in self.dic:
                    self.dic[abbrev] = 1
                else:
                    self.dic[abbrev] += 1


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if not word: return True

        if len(word) <= 2:
            abbrev = word
        else:
            abbrev = word[0] + str(len(word) - 2) + word[-1]

        if abbrev not in self.dic:
            return True
        else:
            if self.dic[abbrev] > 1:
                return False
            else:
                return word in self.wordset



vwa = ValidWordAbbr(['dog','dig'])
print vwa.isUnique('dig')



# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")