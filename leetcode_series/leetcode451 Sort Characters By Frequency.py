# this one should be marked easy.
class Solution(object):
    def frequencySort(self, s):

        dick = {}
        for letter in s:
            if letter not in dick:
                dick[letter] = 1
            else:
                dick[letter] += 1

        order = []
        for letter in dick:
            order.append([dick[letter], letter])
        order.sort()
        order.reverse()

        ans = []
        for item in order:
            for i in xrange(item[0]):
                ans.append(item[1])

        return ''.join(ans)