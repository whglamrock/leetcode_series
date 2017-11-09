
class Solution(object):
    def validWordSquare(self, words):

        if len(words) != len(words[0]): return False

        n = len(words)
        for i in xrange(n):
            col = []
            for j in xrange(n):
                if i < len(words[j]):
                    col.append(words[j][i])
            colword = ''.join(col)
            if colword != words[i]: return False

        return True