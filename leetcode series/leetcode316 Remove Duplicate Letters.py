# see explanation from: https://discuss.leetcode.com/topic/31413/easy-to-understand-iterative-java-solution
class Solution(object):
    def removeDuplicateLetters(self, s):

        if (not s) or len(s) <= 1: return s

        lastpo = {}
        for i in xrange(len(s)):
            lastpo[s[i]] = i

        def findminlastpo(lastpo):
            if (not lastpo):
                return -1
            minlastpo = 2147483647
            for po in lastpo.values():
                minlastpo = min(minlastpo, po)
            return minlastpo

        res = []
        start = 0
        for i in xrange(len(lastpo)):
            minchar = '{'
            end = findminlastpo(lastpo)
            for j in xrange(start, end + 1):
                if s[j] in lastpo and s[j] < minchar:
                    minchar = s[j]
                    start = j + 1
            res.append(minchar)
            del lastpo[minchar]

        return ''.join(res)