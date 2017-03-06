
class Solution(object):
    def findWords(self, words):

        rows = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        ans = []
        for word in words:
            if not word: continue
            firstletter = word[0]
            if firstletter in rows[0]:
                index = 0
            elif firstletter in rows[1]:
                index = 1
            elif firstletter in rows[2]:
                index = 2
            else:
                continue
            for letter in word:
                if letter not in rows[index]:
                    break
            else:
                ans.append(word)

        return ans