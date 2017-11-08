
# if the requirement is "using constant space", then it's become medium or hard question.

class Solution(object):
    def firstUniqChar(self, s):

        dick = {}
        for letter in s:
            if letter not in dick:
                dick[letter] = 1
            else:
                dick[letter] += 1

        for i in xrange(len(s)):
            if dick[s[i]] == 1:
                return i

        return -1