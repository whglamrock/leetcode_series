
# remember how to sort by multiple keys

class Solution(object):
    def findLongestWord(self, s, d):

        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            j = 0
            for char in s:
                if char == word[j]:
                    j += 1
                if j == len(word):
                    return word

        return ''