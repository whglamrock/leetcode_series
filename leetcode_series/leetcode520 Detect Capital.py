
# as tricky as fuck...

class Solution(object):
    def detectCapitalUse(self, word):

        if not word:
            return True

        return word.isupper() or word.islower() or word.istitle()



'''
class Solution(object):
    def detectCapitalUse(self, word):

        if not word:
            return True

        if 'A' <= word[0] <= 'Z':
            if len(word) == 1:
                return True
            if 'A' <= word[1] <= 'Z':
                for i in xrange(2, len(word)):
                    if not 'A' <= word[i] <= 'Z':
                        return False
                return True
            else:
                for i in xrange(2, len(word)):
                    if not 'a' <= word[i] <= 'z':
                        return False
                return True
        else:
            for i in xrange(len(word)):
                if not 'a' <= word[i] <= 'z':
                    return False
            return True
'''